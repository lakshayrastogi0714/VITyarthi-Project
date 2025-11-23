A command-line application simulating basic Automated Teller Machine (ATM) functionalities. This project demonstrates reading and writing persistent data using the built-in Python csv module for account management.

Features

Data Persistence: Account details (ID, Name, PIN, Balance) are stored and updated in a accounts.csv file, ensuring data changes persist between sessions.
Core ATM Services: Offers four main functions:
Cash Withdrawal: Deducts amount after checking for sufficient balance.
Cash Deposit: Adds amount to the current balance.
Change PIN: Allows the user to update their 4-digit PIN.
Account Profile: Displays the current account details and balance.

Security & Validation:

Requires Account ID and PIN validation for all sensitive transactions (Withdrawal, Profile Check).

Checks for Insufficient Balance during withdrawals.

Validates all monetary inputs to ensure they are positive numerical values.

Technologies Used
Language: Python 3.x
Libraries: csv (Standard Library for file handling), sys (For controlled program exit).
Data Storage: CSV File (Comma Separated Values).

How to Run:
Setup:
The initial part of the provided script automatically creates the necessary accounts.csv file with sample data.

a. Save the Code: Save the entire provided code block into a single file named atm_simulator.py.
b. Initial Run: The first time you execute the file, it will create the accounts.csv file in the same directory.

2. Execution
Open your terminal or command prompt, navigate to the directory where you saved atm_simulator.py, and run:

python atm_simulator.py

3. Sample Account Data:
Use the following sample IDs and PINs to test the system:

[ACC_ID, NAME, PIN, BALANCE] [1001, ANMOL, 1204, 120456880.00]

Instructions for Use:
Upon execution, the main menu will appear:

Select a Service: Enter the number corresponding to the service you wish to use (1-4).
Enter Account ID: Provide the Account ID (e.g., 1001).
PIN Validation: If the service requires it (Withdrawal, Profile Check), enter your PIN.
Complete Transaction: Follow the prompts to finalize the action.

Important: Any balance change or PIN update is immediately written back to the accounts.csv file, saving your data for the next run.
