from agents.base_agent import TraderAgent

class MomentumTrader(TraderAgent):
    def __init__(self, name, cash=1000):
        super().__init__(name, cash)
        self.last_price = None

    def decide(self, price, llm_signal):
        if self.last_price is None:
            self.last_price = price
            return "HOLD"

        decision = "HOLD"
        
        if price > self.last_price:
            decision = "BUY"
        
        elif price < self.last_price:
            decision = "SELL"

        self.last_price = price
        return decision

