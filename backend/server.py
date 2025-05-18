from datetime import date
from typing import List
from fastapi import FastAPI, HTTPException
import db_helper
from pydantic import BaseModel


# #To run these api's you have do this first -
# #PS C:\Users\mbarapatre> cd C:\Users\mbarapatre\Downloads\codebasics_python_course_code\Project_expense_management\backend
# C:\Users\mbarapatre\Downloads\codebasics_python_course_code\Project_expense_management\backend> uvicorn server:app
# --reload
class Expense(BaseModel):
    category: str
    amount: float
    notes: str


class Dates(BaseModel):
    start_date: date
    end_date: date


app = FastAPI()


@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    exp = db_helper.fetch_expenses_for_date(expense_date)
    if exp is None:
        raise HTTPException(status_code=500, detail="Fail to retrieve expenses")
    return exp


@app.post("/expenses/{expense_date}")
def update_expenses(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)

    return {"message": "Updated successfully"}


@app.post("/analytics/")
def get_analytics(dates: Dates):
    data = db_helper.fetch_expense_summary(dates.start_date, dates.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Fail to retrieve expense summary")

    breakdown ={}
    total = 0
    total = sum([row['spending']for row in data])
    for row in data:
        percent = (row['spending']/total)*100 if total !=0 else 0
        breakdown[row['category']]={
            "Total":row['spending'],
            "Percentage": round(percent, 2)
        }

    return breakdown


