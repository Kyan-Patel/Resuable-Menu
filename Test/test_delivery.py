import unittest

from src.OrderSystem import OrderSystem


def configSimpleMenu(orderSystem):
    orderSystem.addItemToMenu({'name': 'item1', 'cost': 4.99})
    orderSystem.addItemToMenu({'name': 'item2', 'cost': 5.99})
    orderSystem.addItemToMenu({'name': 'item3', 'cost': 6.99})
    orderSystem.addItemToMenu({'name': 'item4', 'cost': 7.99})


class DeliveryOrder(unittest.TestCase):
    def test_one(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.addItemToCurrentTransaction(1)
        oOrderSystem.setTransactionDelivery(True)
        self.assertAlmostEqual(12.08, oOrderSystem.calcTotalCost(), 2)

    def test_two(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.addItemToCurrentTransaction(2)
        oOrderSystem.setTransactionDelivery(True)
        self.assertAlmostEqual(13.18, oOrderSystem.calcTotalCost(), 2)

    def test_three(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.addItemToCurrentTransaction(3)
        oOrderSystem.setTransactionDelivery(True)
        self.assertAlmostEqual(14.28, oOrderSystem.calcTotalCost(), 2)

    def test_four(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.addItemToCurrentTransaction(4)
        oOrderSystem.setTransactionDelivery(True)
        self.assertAlmostEqual(15.38, oOrderSystem.calcTotalCost(), 2)


if __name__ == '__main__':
    unittest.main()
