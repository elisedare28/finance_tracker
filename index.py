import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import openpyxl


engine = create_engine('mysql+mysqldb://root:1234@localhost/finance_tracker')

def insert_transactions(engine, Transactions):
    transactions_df = pd.DataFrame(Transactions)
    transactions_df.to_sql('Transactions', con=engine, if_exists='append', index=False)

def fetch_categories(engine):
    query = "SELECT * FROM Categories"
    categories = pd.read_sql(query, con=engine)
    return categories

def fetch_transactions(engine):
    query = "SELECT * FROM transactions"
    transactions = pd.read_sql(query, con=engine)
    return transactions

def display_categories(Categories):
    print("\nAvailable Categories:")
    for index, row in Categories.iterrows():
        print(f"{row['CategoryID']}: {row['CategoryName']}")

def add_new_transaction(engine):
    categories = fetch_categories(engine)
    display_categories(categories)
    
    try:
        category_id = int(input("Enter Category ID: "))
        transaction_date = input("Enter Transaction Date (DD-MM-YYYY): ")
        description = input("Enter Description: ")
        amount = float(input("Enter Amount: "))

        try:
            transaction_date = datetime.strptime(transaction_date, '%d-%m-%Y').strftime('%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Please enter the date in DD-MM-YYYY format.")

        transaction = {
            'CategoryID': category_id,
            'TransactionDate': transaction_date,
            'Description': description,
            'Amount': amount
        }

        insert_transactions(engine, [transaction])
        print("Transaction added successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def generate_excel_report(engine):
    transactions = fetch_transactions(engine)

    with pd.ExcelWriter('finance_report.xlsx', engine='openpyxl') as writer:
        transactions.to_excel(writer, sheet_name='Transactions', index=False)
    
    print("Excel report generated successfully!")
    
def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add New Transaction")
        print("2. Generate Excel Report")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_transaction(engine)
        elif choice == '2':
            generate_excel_report(engine)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()