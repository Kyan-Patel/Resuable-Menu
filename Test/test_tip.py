import unittest

from src.OrderSystem import OrderSystem


def configSimpleMenu(orderSystem):
    orderSystem.addItemToMenu({'name': 'item1', 'cost': 1.99})
    orderSystem.addItemToMenu({'name': 'item2', 'cost': 2.99})
    orderSystem.addItemToMenu({'name': 'item3', 'cost': 3.99})
    orderSystem.addItemToMenu({'name': 'item4', 'cost': 4.99})
    orderSystem.addItemToMenu({'name': 'item4', 'cost': 5.99})


class SimpleTip(unittest.TestCase):

    def test_one(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.setTransactionTip(.10)
        oOrderSystem.addItemToCurrentTransaction(1)
        self.assertAlmostEqual(2.39, oOrderSystem.calcTotalCost(), 2)

    def test_two(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)
        oOrderSystem.createNewTransaction()
        oOrderSystem.setTransactionTip(.15)
        oOrderSystem.addItemToCurrentTransaction(2)
        self.assertAlmostEqual(3.74, oOrderSystem.calcTotalCost(), 2)

    def test_three(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.setTransactionTip(.20)
        oOrderSystem.addItemToCurrentTransaction(3)
        self.assertAlmostEqual(5.19, oOrderSystem.calcTotalCost(), 2)

    def test_four(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.setTransactionTip(.25)
        oOrderSystem.addItemToCurrentTransaction(4)
        self.assertAlmostEqual(6.74, oOrderSystem.calcTotalCost(), 2)

    def test_five(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.setTransactionTip(.25)
        oOrderSystem.addItemToCurrentTransaction(4)

        oOrderSystem.createNewTransaction()
        oOrderSystem.setTransactionTip(.15)
        oOrderSystem.addItemToCurrentTransaction(1)

        self.assertAlmostEqual(9.22, oOrderSystem.calcTotalCost(), 2)


if __name__ == '__main__':
    unittest.main()
