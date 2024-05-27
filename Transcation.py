class Transaction:
    def __init__(self):
        # Initialize transaction attributes
        self.items = []  # List to store items in the transaction
        self.is_delivery = False  # Flag to indicate if delivery is included
        self.tip_percentage = 0.0  # Percentage of tip

    def addItem(self, item):
        # Add an item to the transaction
        self.items.append(item)

    def setDelivery(self, is_delivery):
        # Set the delivery status for the transaction
        self.is_delivery = is_delivery

    def setTip(self, tip_percentage):
        # Set the tip percentage for the transaction
        self.tip_percentage = tip_percentage

    def calcTotalCost(self):
        # Calculate the total cost of the transaction
        total_cost = sum(item['cost'] for item in self.items)  # Calculate subtotal
        if self.is_delivery:
            total_cost += 5.99  # Add delivery fee if applicable
        total_cost *= 1.10  # Apply 10% tax
        total_cost += total_cost * self.tip_percentage  # Apply tip
        return total_cost
