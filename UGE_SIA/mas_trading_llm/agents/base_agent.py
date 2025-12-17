class TraderAgent:
    def __init__(self, name, cash=1000):
        self.name = name
        self.initial_cash = cash
        self.cash = cash
        self.asset = 0
        self.num_trades = 0

    def decide(self, price, llm_signal):
        raise NotImplementedError

    def act(self, price, llm_signal):
        decision = self.decide(price, llm_signal)

        if decision == "BUY" and self.cash >= price:
            self.asset += 1
            self.cash -= price
            self.num_trades += 1
            return 1

        if decision == "SELL" and self.asset > 0:
            self.asset -= 1
            self.cash += price
            self.num_trades += 1
            return -1

        return 0

