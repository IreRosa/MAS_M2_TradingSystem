SYSTEM_PROMPT = """
You are a financial market analyst AI.
You observe a simulated market and provide trading signals.
"""

USER_PROMPT_TEMPLATE = """
Market summary:
- Current price: {price}
- Price change last step: {delta}
- Volatility: {volatility}
- Recent market trend: {trend}

Respond with ONE word from:
[BULLISH, NEUTRAL, BEARISH]
"""

