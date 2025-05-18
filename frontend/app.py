# How to run this code
# go till frontend directory - cd C:\barapatre\Downloads\codebasics_python_course_code\Project_expense_management\frontend
# and type "streamlit run .\app.py
# Local URL: http://localhost:8501
# Network URL: http://172.20.10.6:8501
from datetime import datetime

import streamlit as st
from add_update_ui import add_update_tab
from analystics_ui import analytics_tab

API_URL = "http://127.0.0.1:8000"
st.title("Expense_Management_System")
tab1, tab2 = st.tabs(["Add/Update","Data Analyses"])
with tab1:
    add_update_tab()
with tab2:
    analytics_tab()
