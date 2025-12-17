from market.market import Market
from llm.llm_advisor import LLMAdvisor

from agents.random_trader import RandomTrader
from agents.momentum_trader import MomentumTrader
from agents.fundamental_trader import FundamentalTrader
from agents.risk_averse_trader import RiskAverseTrader
from agents.llm_trader import LLMTrader

market = Market()
llm = LLMAdvisor()
llm_trader = LLMTrader("LLMTrader", llm) #standard initialization of events and uses

agents = [
    RandomTrader("Random"),
    MomentumTrader("Momentum"),
    FundamentalTrader("Fundamental", fair_price=105),
    RiskAverseTrader("RiskAverse"),
    llm_trader,
] #declaration of all the traders 

LLM_INTERVAL = 2 

for t in range(100):
    price = market.price
    delta = market.history[-1] - market.history[-2] if len(market.history) > 1 else 0
    vol = market.volatility()
    trend = market.recent_trend(5)  #Determining whether the system increases, decreases or is currently stable 

    if t % LLM_INTERVAL == 0:
        signal = llm.advise(price, delta, vol, trend)
    else:
        signal = llm.last_signal

    net_demand = sum(agent.act(price, signal) for agent in agents)
    market.step(net_demand)

    print(f"t={t:02d} | price={market.price:.2f} | LLM={signal} | demand={net_demand} | trend={trend}")

#Simple output of the final results
print("\n=== FINAL RESULTS ===")
final_price = market.price
for agent in agents:
    pnl = agent.cash + agent.asset * final_price - agent.initial_cash
    print(
        f"{agent.name:12} | Cash: {agent.cash:8.2f} | Inventory: {agent.asset:2d} | Trades: {agent.num_trades:3d} | PnL: {pnl:8.2f}"
    )

import csv
import os

final_price = market.price
csv_file = "simulation_results.csv"

# If the file doesn't exist, we create it 
if not os.path.isfile(csv_file):
    with open(csv_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Simulation",
            "Random_Cash", "Momentum_Cash", "Fundamental_Cash", "RiskAverse_Cash", "LLMTrader_Cash",
            "Random_Inventory", "Momentum_Inventory", "Fundamental_Inventory", "RiskAverse_Inventory", "LLMTrader_Inventory",
            "Random_PnL", "Momentum_PnL", "Fundamental_PnL", "RiskAverse_PnL", "LLMTrader_PnL"
        ])


if os.path.isfile(csv_file):
    with open(csv_file, mode="r", newline="") as f:
        reader = csv.reader(f)
        next(reader)  
        simulation_number = sum(1 for _ in reader) + 1
else:
    simulation_number = 1


with open(csv_file, mode="a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        simulation_number,
        *[agent.cash for agent in agents],
        *[agent.asset for agent in agents],
        *[agent.cash + agent.asset*final_price - agent.initial_cash for agent in agents]
    ])

