import unittest

from src.OrderSystem import OrderSystem


def configSimpleMenu(orderSystem):
    orderSystem.addItemToMenu({'name': 'item1', 'cost': 1.99})
    orderSystem.addItemToMenu({'name': 'item2', 'cost': 2.99})
    orderSystem.addItemToMenu({'name': 'item3', 'cost': 3.99})
    orderSystem.addItemToMenu({'name': 'item4', 'cost': 4.99})
    orderSystem.addItemToMenu({'name': 'item4', 'cost': 5.99})
    orderSystem.addItemToMenu({'name': 'item4', 'cost': 6.99})


class SimpleTip(unittest.TestCase):

    def test_one(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.setTransactionTip(.10)
        oOrderSystem.setTransactionDelivery(True)
        oOrderSystem.addItemToCurrentTransaction(1)
        self.assertAlmostEqual(8.98, oOrderSystem.calcTotalCost(), 2)

    def test_two(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)
        oOrderSystem.createNewTransaction()
        oOrderSystem.setTransactionTip(.15)
        oOrderSystem.setTransactionDelivery(True)
        oOrderSystem.addItemToCurrentTransaction(2)
        self.assertAlmostEqual(10.33, oOrderSystem.calcTotalCost(), 2)

    def test_three(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.setTransactionTip(.20)
        oOrderSystem.setTransactionDelivery(True)
        oOrderSystem.addItemToCurrentTransaction(2)
        self.assertAlmostEqual(10.48, oOrderSystem.calcTotalCost(), 2)

    def test_four(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.setTransactionTip(.25)
        oOrderSystem.setTransactionDelivery(True)
        oOrderSystem.addItemToCurrentTransaction(3)
        oOrderSystem.addItemToCurrentTransaction(4)
        self.assertAlmostEqual(18.71, oOrderSystem.calcTotalCost(), 2)

    def test_five(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.setTransactionTip(.25)
        oOrderSystem.addItemToCurrentTransaction(4)

        oOrderSystem.createNewTransaction()
        oOrderSystem.setTransactionTip(.15)
        oOrderSystem.setTransactionDelivery(True)
        oOrderSystem.addItemToCurrentTransaction(1)

        self.assertAlmostEqual(15.81, oOrderSystem.calcTotalCost(), 2)


if __name__ == '__main__':
    unittest.main()
