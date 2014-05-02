
import abc


class Money(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    @property
    def amount(self):
        return self._amount

    def currency(self):
        return self._currency

    def equals(self, money):
        return self._amount == money.amount and type(self) == type(money)

    @abc.abstractmethod
    def times(self, multiplier):
        return

    @staticmethod
    def dollar(amount):
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Franc(amount, 'CHF')


class Dollar(Money):

    def __init__(self, amount, currency):
        super(Dollar, self).__init__(amount, currency)

    def times(self, multiplier):
        return Money.dollar(self._amount * multiplier)


class Franc(Money):

    def __init__(self, amount, currency):
        super(Franc, self).__init__(amount, currency)

    def times(self, multiplier):
        return Money.franc(self._amount * multiplier)
