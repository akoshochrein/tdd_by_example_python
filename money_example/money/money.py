

class Money(object):

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

    @staticmethod
    def dollar(amount):
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Franc(amount, 'CHF')


class Dollar(Money):

    def __init__(self, amount, currency):
        super(Dollar, self).__init__(amount, currency)


class Franc(Money):

    def __init__(self, amount, currency):
        super(Franc, self).__init__(amount, currency)
