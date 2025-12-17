from agents.base_agent import TraderAgent

class FundamentalTrader(TraderAgent):
    def __init__(self, name, fair_price=100):
        super().__init__(name)
        self.fair_price = fair_price

    def decide(self, price, llm_signal):
        if price < self.fair_price:
            return "BUY"
        if price > self.fair_price:
            return "SELL"
        return "HOLD"
