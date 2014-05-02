
import unittest2
from money.money import Dollar


class TestMoney(unittest2.TestCase):

    def setUp(self):
        pass

    def test_multiplication(self):
        five = Dollar(6)
        five.times(2)
        self.assertEquals(12, five.amount)

if __name__ == '__main__':
    unittest2.main()
