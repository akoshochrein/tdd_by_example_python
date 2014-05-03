
import unittest2
from money.money import Money, Bank, Sum


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
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        reduced = bank.reduce(sum, 'USD')
        self.assertTrue(reduced.equals(Money.dollar(7)))

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), 'USD')
        self.assertTrue(Money.dollar(1).equals(result))

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result = bank.reduce(Money.franc(2), 'USD')
        self.assertTrue(Money.dollar(1).equals(result))

    def test_identity_rate(self):
        self.assertEquals(1, Bank().rate('USD', 'USD'))

    def test_mixed_addition(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result = bank.reduce(five_bucks.plus(ten_francs), 'USD')
        self.assertTrue(result.equals(Money.dollar(10)))

    def test_sum_plus_money(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        sum = Sum(five_bucks, ten_francs).plus(five_bucks)
        result = bank.reduce(sum, 'USD')
        self.assertTrue(result.equals(Money.dollar(15)))

    def test_sum_times(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        sum = Sum(five_bucks, ten_francs).times(2)
        result = bank.reduce(sum, 'USD')
        self.assertTrue(result.equals(Money.dollar(20)))


if __name__ == '__main__':
    unittest2.main()
