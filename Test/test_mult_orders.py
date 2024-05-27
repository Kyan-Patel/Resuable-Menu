import unittest

from src.OrderSystem import OrderSystem


def configSimpleMenu(orderSystem):
    orderSystem.addItemToMenu({'name': 'item1', 'cost': 1.99})
    orderSystem.addItemToMenu({'name': 'item2', 'cost': 2.99})
    orderSystem.addItemToMenu({'name': 'item3', 'cost': 3.99})
    orderSystem.addItemToMenu({'name': 'item4', 'cost': 4.99})


class MultOrders(unittest.TestCase):

    def test_one(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.addItemToCurrentTransaction(1)
        oOrderSystem.addItemToCurrentTransaction(1)
        self.assertAlmostEqual(4.38, oOrderSystem.calcTotalCost(), 2)

    def test_two(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.addItemToCurrentTransaction(1)
        oOrderSystem.addItemToCurrentTransaction(2)
        self.assertAlmostEqual(5.48, oOrderSystem.calcTotalCost(), 2)

    def test_three(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.addItemToCurrentTransaction(1)
        oOrderSystem.addItemToCurrentTransaction(2)
        oOrderSystem.addItemToCurrentTransaction(3)
        self.assertAlmostEqual(9.87, oOrderSystem.calcTotalCost(), 2)

    def test_four(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.addItemToCurrentTransaction(1)
        oOrderSystem.addItemToCurrentTransaction(2)
        oOrderSystem.addItemToCurrentTransaction(3)
        oOrderSystem.addItemToCurrentTransaction(4)
        self.assertAlmostEqual(15.36, oOrderSystem.calcTotalCost(), 2)


if __name__ == '__main__':
    unittest.main()
