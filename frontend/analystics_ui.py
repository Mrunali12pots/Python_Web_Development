from datetime import datetime
import requests
import streamlit as st
import pandas as pd
API_URL = "http://127.0.0.1:8000"

def analytics_tab():
    col1,col2= st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 2), label_visibility="collapsed")
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 9, 2), label_visibility="collapsed")

    if st.button("Get Analytics"):
        payload = {
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d")
            }
        response = requests.post(f"{API_URL}/analytics/",json=payload)
        if response.status_code == 200:
            response = response.json()
        else:
            st.error("Failed to retirve Data")
            analyses_summary = 0

        data = {
            "Category":list(response.keys()),
            "Total":[response[category]["Total"] for category in response],
            "Percentage":[response[category]["Percentage"] for category in response]
        }

        df = pd.DataFrame(data)
        df_sorted=df.sort_values(by="Percentage", ascending=False)
        st.title("Expense Breakdown By Category")
        st.bar_chart(data=df_sorted.set_index("Category")["Percentage"])
        st.table(df_sorted)
