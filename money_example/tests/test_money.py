
import unittest2
from money.money import Money, Bank


class TestMoney(unittest2.TestCase):

    def setUp(self):
        pass

    def test_dollar_multiplication(self):
        six = Money.dollar(6)
        self.assertTrue(Money.dollar(12).equals(six.times(2)))
        self.assertTrue(Money.dollar(30).equals(six.times(5)))

    def test_franc_multiplication(self):
        six = Money.franc(6)
        self.assertTrue(Money.franc(12).equals(six.times(2)))
        self.assertTrue(Money.franc(30).equals(six.times(5)))

    def test_dollar_equality(self):
        self.assertTrue(Money.dollar(42).equals(Money.dollar(42)))

    def test_dollar_inequality(self):
        self.assertFalse(Money.dollar(42).equals(Money.dollar(69)))

    def test_franc_dollar_inequality(self):
        self.assertFalse(Money.franc(5).equals(Money.dollar(5)))

    def test_currency(self):
        self.assertEqual('USD', Money.dollar(1).currency())
        self.assertEqual('CHF', Money.franc(1).currency())

    def test_simple_addition(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum, 'USD')
        self.assertTrue(reduced.equals(Money.dollar(10)))

if __name__ == '__main__':
    unittest2.main()
