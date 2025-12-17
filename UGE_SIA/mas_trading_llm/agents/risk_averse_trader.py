from agents.base_agent import TraderAgent

class RiskAverseTrader(TraderAgent):
    def decide(self, price, llm_signal):
        import random

        if llm_signal == "BEARISH":
            return "SELL"

        if llm_signal == "BULLISH" and random.random() < 0.3:
            return "BUY"

        return "HOLD"
