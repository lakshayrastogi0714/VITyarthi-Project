**ATM Management System**

**Python (CSV-Based CLI Application)**

**ATM Management System – Command-Line Python Application**

**Overview of the Project**

This project is a command-line ATM simulator built in Python. It allows users to perform essential banking transactions such as cash withdrawal, cash deposit, PIN change, and profile viewing.
The system uses CSV (Comma Separated Values) files for persistent storage, meaning all account updates—balance changes, PIN updates—are saved permanently and reflected in future sessions.
The purpose of the project is to demonstrate:

**A. Python file handling**

**B. Data persistence**

**C. Input validation**

**D. Modular programming with functions**

**E. Error-handling and user interaction**

**Features:**

**1. Cash Withdrawal**
   
    A. Requires valid Account ID and PIN
    B. Checks for sufficient balance
    C. Deducts the requested amount
    D. Updates balance in accounts.csv
    
**2. Cash Deposit**
   
    A. Accepts only positive numeric values
    B. Updates account balance immediately
    C. Saves changes to CSV in real-time
   
   
**3. PIN Change**

    A. Ensures new PIN is exactly 4 digits
    B. Updates account’s PIN
    C. Saves securely in CSV
   
**4. Account Profile**

    A. Displays Name, Account Number, PIN, and Balance
    B. Access protected by PIN validation
   
**5. Input Validation**

    A. Handles non-numeric service input
    B. Rejects invalid or negative amounts
    C. Validates PIN format
    D. Detects missing/incorrect account IDs

**Security & Validation**

To ensure safe and reliable usage, the system includes:

    Account ID verification
  
    PIN authentication for sensitive actions
  
    Insufficient balance check during withdrawals
  
    Positive numeric validation for deposit/withdrawal
  
    Strict 4-digit format check for PIN changes
  
    Error-handling for invalid input, unrecognized accounts, or corrupted data files
  
**These validations prevent accidental errors and unauthorized access.**

**Technologies / Tools Used**

  **Language:**
  
        Python 3.x
  
  **Libraries:**
  
    csv → for reading/writing account data
    sys → for controlled program exits
  **Data Storage:**
  
    accounts.csv file storing:
      ACC_ID
      NAME
      ACC_NUMBER
      PIN
      BALANCE
  No external dependencies are required.

**Steps to Install & Run the Project**
  1. Install Python
    Make sure Python 3.x is installed:

  3. Prepare the Accounts CSV File
     
     Create a file named accounts.csv in the same folder as your script.
    
      Use this structure:
     
            [ACC_ID 	NAME	 ACC_NUMBER	 PIN	  BALANCE]
            [1001  	 ANMOL	 10196	     1204	 56880.00]
        You may add or modify entries as needed.
  4. Save the Python File
     Save your ATM program as:

         atm.py
  5. Run the Program
     
     Navigate to the folder and execute:
     
          python atm.py

**Instructions for Testing**

When the script runs, you will see:

Welcome to our ATM

1.Cash Withdrawal

2.Change PIN
   
3.Account Profile
 
4.Cash Deposit

Steps to Test: 

    1.Choose a service (1–4)
    2.Enter a valid Account ID (e.g., 1001)
    3.Enter PIN (required for Withdrawal & Profile Check)
    4.Follow the on-screen instructions to complete the transaction
Sample Testing Accounts

    ACC_ID	NAME ACC_NUMBER	PIN	BALANCE
  
    1001	ANMOL	10196 1204	56880.00
    1002	RAM	   19567  1946	 28400.00
    1003    SHYAM   78546 1256   17000.00

Screenshots
Below are example screenshots from the ATM CLI:

1.Cash Withdrawal

<img width="523" height="221" alt="image" src="https://github.com/user-attachments/assets/baa06036-c303-47c2-9b43-047a0f433967" />

2. Change PIN

<img width="525" height="203" alt="image" src="https://github.com/user-attachments/assets/c2ada745-7dc5-4d0e-812c-c82087a0b88d" />

3. Account Profile

<img width="516" height="195" alt="image" src="https://github.com/user-attachments/assets/ba2dee55-891f-47a3-9f64-159bd8d272db" />

4. Cash Deposit

<img width="534" height="197" alt="image" src="https://github.com/user-attachments/assets/ab7bb213-3c49-4b24-ad55-2cab22cd98af" />

**Persistent Data Storage**

Every update made through the ATM (withdrawal, deposit, PIN change) is immediately written back to accounts.csv

This ensures:

    A.No data loss

    B.Real-time account updates

    C.Reliable behaviour over multiple runs

**Future Enhancements** 

You may extend the project by adding:

    A.Transaction history logs

    B.Admin dashboard

    C.Account creation/deletion

    D.GUI interface (Tkinter/PyQt)

    E.Encryption for PIN storage

**Conclusion**

This ATM Management System provides a complete demonstration of:

    A.Python file handling

    B.Data validation

    C.Modular program design

    D.Safe user authentication

    E.Persistent storage using CSV files

It is ideal for academic projects, demonstrations, and learning exercises involving Python fundamentals.
