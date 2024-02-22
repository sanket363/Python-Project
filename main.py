MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    """Prompt the user to deposit an amount greater than zero and return the amount."""
    while True:
        try:
            amount = int(input("What would you like to deposit? \n$"))
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")

def get_number_of_lines():
    """Asks the user for the number of lines to bet on and validates the input."""
    while True:
        try:
            lines = int(input(f"Enter the number of lines to bet on (1 - {MAX_LINES}): \n"))
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Enter a valid number of lines between 1 and {MAX_LINES}.")
        except ValueError:
            print("Please enter a valid integer.")

def get_bet():
    """Prompt the user for a bet amount within the allowed range and return the amount."""
    while True:
        try:
            amount = int(input("Enter the amount to bet on each line? \n$"))
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        except ValueError:
            print("Please enter a valid number.")

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_valid_bet(balance, lines)
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Your total bet amount is equal to: ${total_bet}")

def get_valid_bet(balance, lines):
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            return bet
        print(f"You don't have enough balance to bet that amount, your current balance is {balance}")

    
main()
