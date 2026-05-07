balance = 10000

def check_balance():
    print(f"Your balance is: {balance}")

def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        balance += amount
        print("Deposit successful!")
    except ValueError as e:
        print("Error:", e)

def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        if amount > balance:
            raise Exception("Insufficient balance!")
        balance -= amount
        print("Withdrawal successful!")
    except ValueError as e:
        print("Invalid input:", e)
    except Exception as e:
        print("Error:", e)

def atm():
    while True:
        try:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                check_balance()
            elif choice == 2:
                deposit()
            elif choice == 3:
                withdraw()
            elif choice == 4:
                print("Thank you!")
                break
            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number!")

        finally:
            print("Transaction completed.\n")

# Run program
atm()
