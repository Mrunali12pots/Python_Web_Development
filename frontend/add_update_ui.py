from datetime import datetime
import requests
import streamlit as st

def add_update_tab():
    API_URL = "http://127.0.0.1:8000"
    categories = ["Food", "Rent", "Shopping", "Entertainment", "Other"]
    entered_date = st.date_input("Enter Date", datetime(2024, 8, 1), label_visibility="collapsed")
    response = requests.get(f"{API_URL}/expenses/{entered_date}")
    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error("Failed to retirve Data")
        existing_expenses = 0

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Amount")
        with col2:
            st.subheader("Category")
        with col3:
            st.subheader("Notes")
        expenses =[]
        for i in range(5):
            if i< len(existing_expenses):
                category = existing_expenses[i]["category"]
                amount = existing_expenses[i]["amount"]
                notes = existing_expenses[i]["notes"]
            else:
                category = "Shopping"
                amount = 0.0
                notes = "--"

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(label="Amount", value=amount, step=1.0,key=f"amount_{i}", label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="category",options=categories, index=categories.index(category),key=f"category_{i}", label_visibility="collapsed")
            with col3:
                notes_input = st.text_input(label="Notes", value=notes, key=f"notes_{i}", label_visibility="collapsed")

            expenses.append({
                'category':category_input,
                'amount': amount_input,
                'notes': notes_input
            })

        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount']>0]
            response = requests.post(f"{API_URL}/expenses/{entered_date}" , json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expenses Updated Successfully..!!")
            else:
                st.error("Failed to update expenses..!!")

