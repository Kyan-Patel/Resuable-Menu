import unittest

from src.OrderSystem import OrderSystem


def configSimpleMenu(orderSystem):
    orderSystem.addItemToMenu({'name': 'item1', 'cost': 1.99})
    orderSystem.addItemToMenu({'name': 'item2', 'cost': 2.99})
    orderSystem.addItemToMenu({'name': 'item3', 'cost': 3.99})
    orderSystem.addItemToMenu({'name': 'item4', 'cost': 4.99})
    orderSystem.addItemToMenu({'name': 'item5', 'cost': 5.99})
    orderSystem.addItemToMenu({'name': 'item6', 'cost': 6.99})
    orderSystem.addItemToMenu({'name': 'item7', 'cost': 7.99})


class SimpleOrder(unittest.TestCase):

    def test_itemNum(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()

        with self.assertRaises(ValueError):
            oOrderSystem.addItemToCurrentTransaction(0)

        with self.assertRaises(ValueError):
            oOrderSystem.addItemToCurrentTransaction(8)

        with self.assertRaises(TypeError):
            oOrderSystem.addItemToCurrentTransaction('bologna')

    def test_tip(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.addItemToCurrentTransaction(7)

        with self.assertRaises(TypeError):
            oOrderSystem.setTransactionTip('magma')

        with self.assertRaises(ValueError):
            oOrderSystem.setTransactionTip(-0.01)

        with self.assertRaises(ValueError):
            oOrderSystem.setTransactionTip(0.4)

        with self.assertRaises(TypeError):
            oOrderSystem.setTransactionTip(15)

    def test_delivery(self):
        oOrderSystem = OrderSystem()
        configSimpleMenu(oOrderSystem)

        oOrderSystem.createNewTransaction()
        oOrderSystem.addItemToCurrentTransaction(1)

        with self.assertRaises(TypeError):
            oOrderSystem.setTransactionDelivery('y')

        with self.assertRaises(TypeError):
            oOrderSystem.setTransactionDelivery('n')


if __name__ == '__main__':
    unittest.main()
