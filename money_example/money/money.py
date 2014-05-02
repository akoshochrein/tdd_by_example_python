
class Money(object):

    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def equals(self, money):
        return self._amount == money.amount and type(self) == type(money)


class Dollar(Money):

    def __init__(self, amount):
        super(Dollar, self).__init__(amount)

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc(Money):

    def __init__(self, amount):
        super(Franc, self).__init__(amount)

    def times(self, multiplier):
        return Franc(self._amount * multiplier)
