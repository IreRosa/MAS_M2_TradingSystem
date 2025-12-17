from agents.base_agent import TraderAgent

class LLMTrader(TraderAgent):
    def __init__(self, name, llm, cash=1000):
        super().__init__(name, cash)
        self.llm = llm

    def decide(self, price, llm_signal):
        if llm_signal == "BULLISH":
            return "BUY"
        elif llm_signal == "BEARISH":
            return "SELL"
        return "HOLD"
