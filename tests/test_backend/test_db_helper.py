

from backend import db_helper


def test_fetch_expenses_for_date():
    expense = db_helper.fetch_expenses_for_date("2024-08-15")
    assert len(expense) == 1
    assert expense[0]['amount'] == 10
    assert expense[0]['category'] == 'Shopping'
    assert expense[0]['id'] == 62

def test_fetch_expenses_for_datefor_notpresentDate():
    expense = db_helper.fetch_expenses_for_date("2024-12-15")
    assert len(expense) == 0


def test_expense_summary():
    expense = db_helper.fetch_expense_summary("2024-08-15","2024-09-15" )
    assert len(expense) == 5
