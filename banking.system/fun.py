def withdraw(balance):
    try:
        money = float(input("Enter money for withdrawal: "))

        if money <= 0:
            print("Enter an amount greater than zero.")
        elif balance - money < 2000:
            print("Insufficient balance! Minimum balance of Rs.2000 must be maintained.")
        else:
            balance -= money
            print(f"Rs.{money} is withdrawn successfully!")

    except ValueError:
        print("Invalid amount! Please enter a numeric value.")

    return balance


def deposit(balance):
    try:
        money = float(input("Enter money to deposit: "))

        if money <= 0:
            print("Enter an amount greater than zero.")
        else:
            balance += money
            print(f"Rs.{money} is deposited successfully!")

    except ValueError:
        print("Invalid amount! Please enter a numeric value.")

    return balance


def save_balance(balance):
    with open("balance.txt", "w") as file:
        file.write(str(balance))


def load_balance():
    try:
        with open("balance.txt", "r") as file:
            return float(file.read())

    except FileNotFoundError:
        return 5000
