import unittest

from Transaction import Transaction
from src.OrderSystem import OrderSystem


def configSimpleMenu(orderSystem):
    orderSystem.addItemToMenu({'name': 'item1', 'cost': 1.99})
    orderSystem.addItemToMenu({'name': 'item2', 'cost': 2.99})
    orderSystem.addItemToMenu({'name': 'item3', 'cost': 3.99})
    orderSystem.addItemToMenu({'name': 'item4', 'cost': 4.99})
    orderSystem.addItemToMenu({'name': 'item4', 'cost': 5.99})


class SimpleTransaction(unittest.TestCase):

    def test_one(self):
        oTransaction = Transaction()
        oTransaction.setTip(.10)
        oTransaction.setDelivery(True)
        oTransaction.addItem({'name': 'item1', 'cost': 1.99})
        self.assertAlmostEqual(8.98, oTransaction.calcTotalCost(), 2)

    def test_two(self):
        oTransaction = Transaction()
        oTransaction.setTip(.10)
        oTransaction.addItem({'name': 'item2', 'cost': 2.99})
        self.assertAlmostEqual(3.59, oTransaction.calcTotalCost(), 2)

    def test_three(self):
        oTransaction = Transaction()
        oTransaction.setTip(.10)
        oTransaction.setDelivery(True)
        oTransaction.addItem({'name': 'item3', 'cost': 3.99})
        self.assertAlmostEqual(11.38, oTransaction.calcTotalCost(), 2)

    def test_four(self):
        oTransaction = Transaction()
        oTransaction.setTip(.15)
        oTransaction.addItem({'name': 'item4', 'cost': 4.99})
        oTransaction.addItem({'name': 'item3', 'cost': 3.99})
        self.assertAlmostEqual(11.22, oTransaction.calcTotalCost(), 2)

    def test_five(self):
        oTransaction = Transaction()
        oTransaction.setTip(.15)
        oTransaction.setDelivery(True)
        oTransaction.addItem({'name': 'item5', 'cost': 5.99})
        oTransaction.addItem({'name': 'item3', 'cost': 3.99})
        self.assertAlmostEqual(19.06, oTransaction.calcTotalCost(), 2)


if __name__ == '__main__':
    unittest.main()
