import os
from dotenv import load_dotenv
load_dotenv()

from google import genai
from llm.prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE


class LLMAdvisor:
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("Missing GEMINI_API_KEY in .env")

        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name
        self.last_signal = "NEUTRAL"

    def advise(self, price, delta, volatility, trend):
        user_prompt = USER_PROMPT_TEMPLATE.format(
            price=price, delta=delta, volatility=volatility, trend=trend
        )
        full_prompt = f"{SYSTEM_PROMPT.strip()}\n\n{user_prompt.strip()}"

        try:
            resp = self.client.models.generate_content(
                model=self.model_name,
                contents=full_prompt,
            )
            text = (resp.text or "").strip().upper()
        except Exception:
            print("LLM unavailable, using last signal")
            return self.last_signal

        if "BULLISH" in text:
            self.last_signal = "BULLISH"
        elif "BEARISH" in text:
            self.last_signal = "BEARISH"
        else:
            self.last_signal = "NEUTRAL"

        return self.last_signal