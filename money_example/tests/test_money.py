
import unittest2
from money.money import Money


class TestMoney(unittest2.TestCase):

    def setUp(self):
        pass

    def test_dollar_multiplication(self):
        five = Money.dollar(6)
        self.assertTrue(Money.dollar(12).equals(five.times(2)))
        self.assertTrue(Money.dollar(30).equals(five.times(5)))

    def test_franc_multiplication(self):
        five = Money.franc(6)
        self.assertTrue(Money.franc(12).equals(five.times(2)))
        self.assertTrue(Money.franc(30).equals(five.times(5)))

    def test_dollar_equality(self):
        self.assertTrue(Money.dollar(42).equals(Money.dollar(42)))

    def test_dollar_inequality(self):
        self.assertFalse(Money.dollar(42).equals(Money.dollar(69)))

    def test_franc_equality(self):
        self.assertTrue(Money.franc(42).equals(Money.franc(42)))

    def test_franc_inequality(self):
        self.assertFalse(Money.franc(42).equals(Money.franc(69)))

    def test_franc_dollar_inequality(self):
        self.assertFalse(Money.franc(5).equals(Money.dollar(5)))

if __name__ == '__main__':
    unittest2.main()
