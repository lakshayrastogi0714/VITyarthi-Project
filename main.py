import csv
import sys

def load_data(file_name='accounts.csv'):
    """Reads all account data from the CSV file into a list of dictionaries."""
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: Account data file '{file_name}' not found. Please ensure the file exists.")
        sys.exit()
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        sys.exit()

def save_data(data, file_name='accounts.csv'):
    """Writes the updated list of account dictionaries back to the CSV file."""
    if not data:
        return
    
    # Ensure the correct header order is maintained
    fieldnames = ['ACC_ID', 'NAME', 'ACC_NUMBER', 'PIN', 'BALANCE']
    try:
        with open(file_name, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader() 
            writer.writerows(data)
    except Exception as e:
        print(f"An error occurred while saving data: {e}")
        sys.exit()

def find_account(data, acc_id):
    """Finds and returns the account dictionary for a given ACC_ID."""
    for account in data:
        # Match the string ACC_ID in the file with the integer input
        if account['ACC_ID'] == str(acc_id):
            return account
    return None

# --- Main ATM Logic ---

def run_atm():
    print("\nWelcome to our ATM")
    print("Our Services:")
    print("1. Cash Withdrawal")
    print("2. Change PIN")
    print("3. Account Profile")
    print("4. Cash Deposit")

    # 1. Input validation for service selection
    try:
        service_input = input("Which service do you want to opt? (1-4): ")
        service = int(service_input)
        if service not in [1, 2, 3, 4]:
            raise ValueError("Invalid service option.")
    except ValueError as e:
        print(f"Invalid input. Please enter a number between 1 and 4.")
        sys.exit()

    # 2. Get Account ID and load data
    try:
        acc_id = int(input("Please Enter Your Account ID: "))
    except ValueError:
        print("Invalid Account ID format.")
        sys.exit()

    # Load all account data from the file
    all_accounts = load_data()
    # Find the specific user's account
    current_account = find_account(all_accounts, acc_id)

    if not current_account:
        print(f"Account with ID {acc_id} not found.")
        return

    # 3. Perform the selected service
    
    # CASH WITHDRAWAL (Service 1)
    if service == 1:
        # PIN Validation Added Here
        entered_pin = input("Please Enter Your PIN: ")
        
        if entered_pin != current_account['PIN']:
            print("Transaction Failed: Invalid PIN.")
            return

        try:
            amount = float(input("Enter The Amount: "))
            current_balance = float(current_account['BALANCE'])
            
            if amount > current_balance:
                print("Transaction Failed: Insufficient Balance.")
            elif amount <= 0:
                print("Transaction Failed: Amount must be positive.")
            else:
                new_balance = current_balance - amount
                # Update the balance in the dictionary, formatted to 2 decimal places
                current_account['BALANCE'] = f"{new_balance:.2f}" 
                save_data(all_accounts) # Save the updated data back to file
                print(f"Updated Profile: {list(current_account.values())}")
                print("Transaction completed successfully.")

        except ValueError:
            print("Invalid amount format. Please enter a valid number.")
            
    # CHANGE PIN (Service 2)
    elif service == 2:
        new_pin = input("Please Enter Your New PIN (4 digits): ")
        if len(new_pin) == 4 and new_pin.isdigit():
            current_account['PIN'] = new_pin
            save_data(all_accounts)
            print(f"Updated Profile: {list(current_account.values())}")
            print("Transaction completed successfully.")
        else:
            print("Invalid PIN format. PIN must be 4 digits.")
            
    # ACCOUNT PROFILE (Service 3)
    elif service == 3:
        # PIN Validation for Profile Check
        entered_pin = input("Please Enter Your PIN to view profile: ")
        
        if entered_pin != current_account['PIN']:
            print("Access Denied: Invalid PIN.")
            return

        print(f"Account Profile: {list(current_account.values())}")
        print("Transaction completed successfully.")

    # CASH DEPOSIT (Service 4)
    elif service == 4:
        try:
            cash = float(input("Please Enter The Amount to be Deposited: "))
            if cash <= 0:
                print("Transaction Failed: Deposit amount must be positive.")
            else:
                current_balance = float(current_account['BALANCE'])
                new_balance = current_balance + cash
                current_account['BALANCE'] = f"{new_balance:.2f}"
                save_data(all_accounts)
                print(f"Updated Profile: {list(current_account.values())}")
                print("Transaction completed successfully.")
                
        except ValueError:
            print("Invalid amount format. Please enter a valid number.")

# Execute the ATM program
if __name__ == "__main__":
    run_atm()
