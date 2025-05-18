import mysql.connector
from contextlib import contextmanager
from Logging_setup import logger_function

logger = logger_function('db_helper')


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    print("Closing cursor")
    cursor.close()
    connection.close()


def fetch_all_records():
    query = "SELECT * from expenses"

    with get_db_cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)


def fetch_expenses_for_date(expense_date):
    logger.info(f"Ran Method -to fecth expense of date {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)
        return expenses


def insert_expense(expense_date, amount, category, notes):
    logger.info(f"Ran Method -to insert expense of date {expense_date}, amount:{amount}, category:{category},note:{notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


def delete_expenses_for_date(expense_date):
    with get_db_cursor(commit=True) as cursor:
        logger.info(f"Ran Method -to delete expense of date {expense_date}")
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def fetch_expense_summary(start_date, end_date):
    with get_db_cursor() as cursor:
        logger.info(f"ran method to get fetch_expense_summary for start_date:{start_date} to end_date:{end_date}")
        cursor.execute(
            "select category, sum(amount) as spending from expenses where expense_date BETWEEN %s and %s Group by category",
            (start_date, end_date)
        )
        anallytics = cursor.fetchall()
        return anallytics


if __name__ == "__main__":
    # fetch_all_records()
    # fetch_expenses_for_date("2024-08-01")
#     # insert_expense("2024-08-20", 300, "Food", "Panipuri")
#     # delete_expenses_for_date("2024-08-20")
#     # fetch_expenses_for_date("2024-08-20")
    print(fetch_expense_summary("2024-08-20","2024-09-01"))
