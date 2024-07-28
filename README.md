# Personal Finance Tracker

This project is a personal finance tracker built using Python, MySQL, and Excel. It allows the user to manually enter transactions in the Python file, store them in a MySQL database, and generate Excel reports of transactions.

## Features

- Add new transactions manually.
- Store transactions in a MySQL database.
- Generate Excel reports of transactions.

## Technologies Used

- Python
- MySQL
- Pandas
- SQLAlchemy
- Openpyxl

## Setup

### Prerequisites

- Python 3.x
- MySQL
- `pip` (Python package installer)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/finance-tracker.git
    cd finance-tracker
    ```

2. **Install required Python packages:**
    ```bash
    pip install pandas sqlalchemy mysqlclient openpyxl
    ```

3. **Set up MySQL database:**
    - Create a new database in MySQL, e.g., `finance_tracker`.
    - Create the necessary tables:
    ```sql
    CREATE TABLE transactions (
        TransactionID INT AUTO_INCREMENT PRIMARY KEY,
        CategoryID INT,
        TransactionDate DATE,
        Description VARCHAR(255),
        Amount DECIMAL(10, 2)
    );

    CREATE TABLE categories (
        CategoryID INT AUTO_INCREMENT PRIMARY KEY,
        CategoryName VARCHAR(255)
    );

    -- Add some sample categories
    INSERT INTO categories (CategoryName) VALUES ('Groceries'), ('Rent'), ('Utilities'), ('Entertainment'), ('Dining'), ('Miscellaneous');
    ```

4. **Update database connection in `finance_tracker.py`:**
    ```python
    engine = create_engine('mysql+mysqldb://username:password@localhost/financedb')
    ```

## Usage

1. **Run the script:**
    ```bash
    python finance_tracker.py
    ```

2. **Follow the on-screen menu:**
    - Add new transactions.
    - Generate Excel report.

3. **Find the generated Excel report:**
    - The report will be saved as `finance_report.xlsx` in the project directory.



