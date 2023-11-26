    #davaleba1     ar vici es igulisxmet tu ara
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

user_radius = float(input("Enter the radius of the circle: "))

circle = Circle(user_radius)

perimeter = circle.calculate_perimeter()
area = circle.calculate_area()

print(f"Perimeter: {perimeter}")
print(f"Area: {area}")










    #davaleba2
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "error 404"

calculator = Calculator()

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result_add = calculator.add(num1, num2)
result_subtract = calculator.subtract(num1, num2)
result_multiply = calculator.multiply(num1, num2)
result_divide = calculator.divide(num1, num2)

print(f"Addition +: {result_add}")
print(f"Subtraction -: {result_subtract}")
print(f"Multiplication *: {result_multiply}")
print(f"Division /: {result_divide}")













    #davaleba3
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name):
        if item_name in clothes_inventory:
            if item_name in self.items:
                self.items[item_name]['quantity'] += 1
            else:
                self.items[item_name] = {'price': clothes_inventory[item_name], 'quantity': 1}
            print(f"{item_name} added to the cart.")
        else:
            print(f"Sorry, {item_name} is not available in the inventory.")

    def remove_item(self, item_name):
        if item_name in self.items:
            if self.items[item_name]['quantity'] == 1:
                del self.items[item_name]
            else:
                self.items[item_name]['quantity'] -= 1
            print(f"One {item_name} removed from the cart.")
        else:
            print(f"{item_name} is not in the cart.")

    def display_cart(self):
        if not self.items:
            print("Shopping Cart is empty.")
        else:
            print("Shopping Cart:")
            for item_name, item_info in self.items.items():
                print(f"{item_name} - Quantity: {item_info['quantity']}, Price: ${item_info['price']} each")

    def calculate_total_cost(self):
        total_cost = sum(item_info['price'] * item_info['quantity'] for item_info in self.items.values())
        return total_cost

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write("Shopping Cart:\n")
            for item_name, item_info in self.items.items():
                file.write(f"{item_name} - Quantity: {item_info['quantity']}, Price: ${item_info['price']} each\n")
            total_cost = self.calculate_total_cost()
            file.write(f"\nTotal Cost: ${total_cost}")

clothes_inventory = {
    'T-shirt': 75,
    'Jeans': 150,
    'Sweater': 85,
    'Sneakers': 200,
    'Shorts': 50
}

cart = ShoppingCart()

while True:
    print("\n1. Buy item and add to cart")
    print("2. Remove item from cart")
    print("3. Display cart")
    print("4. Save to file and Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item_name = input("Enter the item name to buy and add to the cart: ")
        cart.add_item(item_name)

    elif choice == '2':
        item_name = input("Enter the item name to remove from the cart: ")
        cart.remove_item(item_name)

    elif choice == '3':
        cart.display_cart()

    elif choice == '4':
        filename = input("Enter the filename to save the cart: ")
        cart.save_to_file(filename)
        print(f"Shopping cart saved to {filename}.txt.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")















    #davaleba4
class BankAccount:
    def __init__(self, account_holder, balance=0, currency='Euro'):
        self.account_holder = account_holder
        self.balance = balance
        self.currency = currency

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} {self.currency}. New balance: {self.balance} {self.currency}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} {self.currency}. New balance: {self.balance} {self.currency}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            print("Insufficient funds. Withdrawal not allowed.")

    def change_currency(self, new_currency):
        if new_currency == 'Euro' or new_currency == 'USD':
            if self.currency == new_currency:
                print(f"The account is already in {new_currency}. No change needed.")
            else:
                if new_currency == 'USD':
                    self.balance *= 1.18
                else:
                    self.balance /= 1.18
                self.currency = new_currency
                print(f"Changed currency to {new_currency}. New balance: {self.balance} {self.currency}")
        else:
            print("Invalid currency. Please choose 'Euro' or 'USD'.")

    def display_balance(self):
        print(f"Balance for {self.account_holder}: {self.balance} {self.currency}")


def main():
    account_holder_name = input("Enter the account holder's name: ")
    initial_balance = float(input("Enter the initial balance: "))
    account_currency = input("Enter the account currency (Euro or USD): ").capitalize()

    account = BankAccount(account_holder_name, initial_balance, account_currency)

    while True:
        print("\n1. Deposit money")
        print("2. Withdraw money")
        print("3. Display balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            deposit_amount = float(input("Enter the amount to deposit: "))
            account.deposit(deposit_amount)

        elif choice == '2':
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(withdraw_amount)

        elif choice == '3':
            account.display_balance()

        elif choice == '4':
            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()







