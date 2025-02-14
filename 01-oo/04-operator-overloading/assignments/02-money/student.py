class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if (self.currency != other.currency):
            raise RuntimeError("Mismatched currencies!")
        else:
            return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if (self.currency != other.currency):
            raise RuntimeError("Mismatched currencies!")
        else:
            return Money(self.amount - other.amount, self.currency)

    def __mul__(self, other):
        return Money(self.amount * other, self.currency)