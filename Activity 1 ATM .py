balance = 5000
deposit_count = 0
withdraw_count = 0
limit = 2000

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter your choice: "))
    amount = int(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")

    elif choice == 1:
        balance = balance + amount
        deposit_count += 1
        print("Deposit successful")

    elif choice == 2:
        if amount > balance:
            print("Insufficient balance")
        elif amount > limit:
            print("Withdrawal limit exceeded")
        else:
            balance = balance - amount
            withdraw_count += 1
            print("Withdrawal successful")

    else:
        print("Invalid choice")

print("\n--- ATM TRANSACTION SUMMARY ---")
print("Final Balance:", balance)
print("Total Deposits:", deposit_count)
print("Total Withdrawals:", withdraw_count)
print("Thank you for using ATM")
