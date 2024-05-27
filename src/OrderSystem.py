class OrderSystem:
    def __init__(self):
        # Initialize OrderSystem attributes
        self.menu = []  # List to store menu items
        self.transactions = []  # List to store transaction objects

    def addItemToMenu(self, item):
        # Add an item to the menu
        if not isinstance(item, dict) or 'name' not in item or 'cost' not in item:
            raise ValueError("Invalid item format. Expected dict with 'name' and 'cost' keys.")
        if not isinstance(item['name'], str):
            raise ValueError("Item name must be a string.")
        if not isinstance(item['cost'], (int, float)):
            raise ValueError("Item cost must be a number.")
        self.menu.append(item)

    def printMenu(self):
        # Print the menu
        for idx, item in enumerate(self.menu, start=1):
            print(f"{idx}. {item['name']}: ${item['cost']}")

    def createNewTransaction(self):
        # Create a new transaction object and append it to the list of transactions
        self.transactions.append(Transaction())

    def addItemToCurrentTransaction(self, item_num):
        # Add an item from the menu to the current transaction
        if not isinstance(item_num, int) or item_num < 1 or item_num > len(self.menu):
            raise ValueError("Invalid item number.")
        self.transactions[-1].addItem(self.menu[item_num - 1])

    def cancelCurrentTransaction(self):
        # Cancel the most recent transaction
        self.transactions.pop()

    def setTransactionDelivery(self, is_delivery):
        # Set the delivery status for the current transaction
        self.transactions[-1].setDelivery(is_delivery)

    def setTransactionTip(self, tip_percentage):
        # Set the tip percentage for the current transaction
        if not isinstance(tip_percentage, float) or tip_percentage < 0.00 or tip_percentage >= 0.40:
            raise ValueError("Invalid tip percentage.")
        self.transactions[-1].setTip(tip_percentage)

    def getTransactionCost(self):
        # Get the cost of the current transaction
        return self.transactions[-1].calcTotalCost()

    def calcTotalCost(self):
        # Calculate the combined cost of all transactions
        total_cost = sum(transaction.calcTotalCost() for transaction in self.transactions)
        return total_cost
