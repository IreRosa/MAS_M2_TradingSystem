import numpy as np

class Market:
    def __init__(self, initial_price=100):
        self.price = initial_price
        self.history = [initial_price]

    def step(self, net_demand):
        noise = np.random.normal(0, 0.5)
        self.price += 0.1 * net_demand + noise
        self.price = max(1, self.price)
        self.history.append(self.price)

    def volatility(self, window=5):
        if len(self.history) < window:
            return 0
        return np.std(self.history[-window:])
        
    def recent_trend(self, n=5):
        if len(self.history) < 2:
            return "STABLE"
        recent_prices = self.history[-n:]
        if recent_prices[-1] > recent_prices[0]:
            return "UP"
        elif recent_prices[-1] < recent_prices[0]:
            return "DOWN"
        else:
            return "STABLE"
