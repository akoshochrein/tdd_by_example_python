
class Dollar(object):

    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)

    def equals(self, dollar):
        return self._amount == dollar.amount


class Franc(object):

    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def times(self, multiplier):
        return Franc(self._amount * multiplier)

    def equals(self, franc):
        return self._amount == franc.amount
