
import unittest2
from money.money import Dollar, Franc


class TestMoney(unittest2.TestCase):

    def setUp(self):
        pass

    def test_dollar_multiplication(self):
        five = Dollar(6)
        self.assertTrue(Dollar(12).equals(five.times(2)))
        self.assertTrue(Dollar(30).equals(five.times(5)))

    def test_franc_multiplication(self):
        five = Franc(6)
        self.assertTrue(Franc(12).equals(five.times(2)))
        self.assertTrue(Franc(30).equals(five.times(5)))

    def test_dollar_equality(self):
        self.assertTrue(Dollar(42).equals(Dollar(42)))

    def test_dollar_inequality(self):
        self.assertFalse(Dollar(42).equals(Dollar(69)))

if __name__ == '__main__':
    unittest2.main()
