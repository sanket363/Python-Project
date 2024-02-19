def deposit():
    while True:
        amount = input("What would you like to deposit? \n$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be a greater than zero")
        else:
            print("Please Enter a number")
    
    return amount

def main():
    balance = deposit()

if __name__ == "__main__":
    main()