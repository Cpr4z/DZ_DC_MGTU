RUBLE = 1
DOLLAR = 60
EURO = 70


class BaseWallet:
    exchange_rate = 1

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def get_name(self):
        return self.name

    def get_amount(self):
        return self.amount

    def get_exchange_cofficient(self):
        return self.exchange_rate

    def to_base(self):
        return self.exchange_rate * self.amount

    def repeating_operation(self, other, operation):
        if isinstance(other, BaseWallet):
            return self.__class__(self.name,
                                  operation(self.to_base(), other.to_base()) / self.exchange_rate)
        return self.__class__(self.name, operation(self.amount, other))

    def __add__(self, other):
        return self.repeating_operation(other, lambda a, b: a + b)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.repeating_operation(other, lambda a, b: a - b)

    def __rsub__(self, other):
        return self.repeating_operation(other, lambda a, b: b - a)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        return self.repeating_operation(other, lambda a, b: a * b)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return self.repeating_operation(other, lambda a, b: a / b)

    def __rtruediv__(self, other):
        return self.repeating_operation(other, lambda a, b: b / a)

    def __eq__(self, other):
        return type(self) is type(other) and self.amount == other.amount

    def __repr__(self):
        return f"{self._log_name} {self.name} {self.amount}"

    def spend_all(self):
        if self.get_amount() > 0:
            self.amount = 0


class RubbleWallet(BaseWallet):
    def __init__(self, name, amount):
        super().__init__(name, amount)
        self.exchange_rate = RUBLE
        self._log_name = "Rubble Wallet"


class DollarWallet(BaseWallet):
    def __init__(self, name, amount):
        super().__init__(name, amount)
        self.exchange_rate = DOLLAR
        self._log_name = "Dollar Wallet"


class EuroWallet(BaseWallet):
    def __init__(self, name, amount):
        super().__init__(name, amount)
        self.exchange_rate = EURO
        self._log_name = "Euro Wallet"
