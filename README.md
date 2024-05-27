# Reusable Delivery Software

## Overview
This project implements a pair of classes for processing transactions consisting of multiple items ordered from a takeout restaurant. It allows users to set up a menu, handle new transactions, and calculate the overall cost of all transactions processed.

## Features
- **Transaction Class**: Manages individual transactions, including adding items, setting delivery status, setting tip percentage, and calculating total cost.
- **OrderSystem Class**: Handles menu management, transaction creation, item addition to transactions, cancellation of transactions, setting delivery and tip for transactions, and calculating total cost of all transactions.

## Showcase of Python Practice
This project showcases several important concepts in Python programming and coding theory and practice, including:
- Object-Oriented Programming (OOP): The project demonstrates the use of classes and objects to model real-world entities (transactions, items, etc.) and encapsulate their behavior and attributes.
- Modular Design: The code is organized into separate files (`Transaction.py` and `OrderSystem.py`) to promote modularity and code reusability.
- Encapsulation: The classes use encapsulation to hide internal implementation details and provide clean interfaces for interacting with the objects.
- Error Handling: Proper error handling and input validation techniques are employed to ensure robustness and reliability of the code.
- Unit Testing: The project includes unit tests to verify the correctness of the implementation and catch potential bugs early in the development process.
- Documentation: Clear and concise documentation (in the form of comments and README) is provided to explain the purpose, usage, and behavior of the classes and methods.

## Setup
1. Clone this repository to your local machine.
2. Navigate to the `src` directory.
3. Run your Python scripts in your preferred development environment.

## Usage
1. Import the `Transaction` and `OrderSystem` classes from the respective files.
2. Create an instance of the `OrderSystem` class.
3. Add items to the menu using the `addItemToMenu` method.
4. Create a new transaction using the `createNewTransaction` method.
5. Add items to the current transaction using the `addItemToCurrentTransaction` method.
6. Set delivery and tip for the current transaction using the respective methods.
7. Calculate the cost of the current transaction using the `getTransactionCost` method.
8. Repeat steps 4-7 for additional transactions.
9. Calculate the total cost of all transactions using the `calcTotalCost` method.

## Testing
Unit tests for the `Transaction` and `OrderSystem` classes are provided in the `tests` directory. You can run the tests to ensure the correctness of the implementation.
