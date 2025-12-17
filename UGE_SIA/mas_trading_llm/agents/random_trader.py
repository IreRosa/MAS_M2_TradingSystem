import random
from agents.base_agent import TraderAgent

class RandomTrader(TraderAgent):
    def decide(self, price, llm_signal):
        return random.choice(["BUY", "SELL", "HOLD"])
