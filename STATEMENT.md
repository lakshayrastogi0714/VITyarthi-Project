Project Statement: CSV-based ATM Simulation

1. Problem Statement

The challenge addressed by this project is the need for a realistic, yet simple, simulation environment to demonstrate fundamental concepts of **financial transaction processing**, **user authentication**, and **persistent data management** within a console application. In real-world systems, any change to a user's balance or profile must be permanent.

This project specifically solves the problem of how to handle transactions and account data changes that must **persist beyond the current session**, using easily accessible file formats and standard Python tools.


2. Scope and Goals

The primary goal is to create a fully functional, command-line ATM interface that manages data using a CSV file.

In Scope

Account Lookup: Identifying a user's record based on a unique Account ID.
Authentication: Verifying a user's identity using a PIN check for sensitive operations.
Core Transactions: Implementing logic for Deposit, Withdrawal, and PIN Change.
Balance Check: Ensuring a withdrawal request does not exceed the current available balance.
File Persistence: Reading all account data from `accounts.csv` at startup and writing updated data back to the file after every successful transaction.
Input Handling: Validating numerical inputs (amounts) and checking PIN length/format.

Out of Scope (Current Limitations)

Security: Hashing or encrypting sensitive data like PINs and Balances.
Complex Error Handling: Advanced logging or handling of concurrent access/race conditions.
User Interface: Graphic user interface (GUI) or web interface.
New Account Creation: The system relies on pre-existing data in the CSV file.

3. Design Rationale

A. Data Structure

CSV File (`accounts.csv`): A CSV file was chosen for simplicity and to easily demonstrate the use of Python's built-in `csv` library for data serialization.
List of Dictionaries: Within the Python code, the CSV data is loaded into a **list of dictionaries**. This structure is ideal because it allows direct access to account properties (like `'PIN'` or `'BALANCE'`) using clear, semantic keys, and the list structure enables easy iteration and searching (`find_account`).

B. Modularity

The code is organized into distinct functions for clarity and maintainability:

load_data(): Handles all file reading and error handling (e.g., `FileNotFoundError`).
save_data(): Handles all file writing, ensuring updated data is correctly formatted and written back to the CSV.
find_account(): Simplifies the process of locating a specific account dictionary within the loaded list.
run_atm(): Contains the core interactive logic, menu display, user flow, and directs the calls to the appropriate transaction logic.

C. Transaction Logic

All transaction functions (Withdrawal, Deposit, PIN Change) follow a standardized pattern:

1.  Read the current balance/PIN (as string from CSV).
2.  Convert string balance to a float for mathematical operations.
3.  Perform the calculation or change.
4.  Convert the new balance back to a string (formatted to two decimal places) for storage.
5.  Call save_data() to ensure the change is permanent.

This process accurately reflects the data flow required for persistent application state.
