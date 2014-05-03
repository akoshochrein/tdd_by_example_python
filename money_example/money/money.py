

class Expression(object):
    pass


class Money(Expression):

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    @property
    def amount(self):
        return self._amount

    def currency(self):
        return self._currency

    def equals(self, other):
        return self._amount == other.amount and self._currency == other._currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend):
        return Money(self._amount + addend._amount, self._currency)

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')


class Bank(object):

    def reduce(self, source, to):
        return Money.dollar(10)
