"""

1. Initialize balance = 1000.00
2. Start a WHILE True loop:
    a. Print Menu (1. Balance, 2. Deposit, 3. Withdraw, 4. Transfer, 5. Exit)
    b. Get user choice
    c. MATCH choice:
        case "1": Print formatted balance
        case "2": Get deposit amt -> Validate it is numeric -> Add to balance
        case "3": Get withdraw amt -> Validate it is numeric -> Check for Overdraft -> Subtract
        case "4": Get transfer amt -> Validate it is numeric -> Check for Overdraft -> Subtract
        case "5": Print goodbye -> Break loop
        case _: Print "Invalid Selection"

    """


balance = 1000.00

while True:
    print("\n\nBank Menu")
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. transfer")
    print("5. Exit")

    choice = input("\n\nWhat would you like to do?:   ")

    match choice:
        case "1":
            print(f"Current Balance: ${balance:,.2f}")
        
        case "2":
            amount = input("Enter deposit amount: ")
            if amount.replace('.', '', 1).isdigit():
                balance += float(amount)
                print(f"Deposited ${float(amount):,.2f}")
            else:
                print("Invalid amount")
        
        case "3":
            amount = input("Enter withdrawal amount:  ")
            if amount.replace('.', '', 1).isdigit():
                amount = float(amount)
                if amount > balance:
                    print("Overdraft! Transaction cancelled ")
                else: 
                    balance -= amount
                    print(f"Withdrew ${amount:,.2f}")
            else:
                print("Invalid amount")

        case "4":
            amount = input("Enter transfer amount:  ")
            if amount.replace('.', '', 1).isdigit():
                amount = float(amount)
                if amount > balance:
                    print("Overdraft! Transfer cancelled. ")
                else:
                    balance -= amount
                    print(f"Transferred ${amount:,.2f}")
            else:
                print("Invalid number")

        case "5":
            print("Goodbye!")
            break

        case _:
            print("Invalid selection")



