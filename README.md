# Expense Management System

A full-stack web application designed to help you **log, categorize, and analyze daily expenses** effortlessly.

Built with:

- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **Database:** MySQL  
- **Testing:** Pytest  

---

## Features

- Add or update daily expenses easily  
- Categorize spending (Food, Rent, Shopping, etc.)  
- Analyze expenses within any date range  
- Visualize spending with bar charts and percentage breakdowns  
- Persistent data storage with MySQL  
- Robust backend logging and automated unit testing  

---

## Project Structure

- **frontend/** — Streamlit UI components (expense entry, analytics)  
- **backend/** — FastAPI routes, database logic, and logging setup  
- **tests/** — Pytest unit tests for backend functions  
- **requirements.txt** — Python dependencies  
- **README.md** — Project documentation  

---

##  How It Works

### Backend (FastAPI)

- Provides API endpoints to fetch, add/update, and summarize expenses  
- Handles database operations securely and efficiently  
- Logs important backend operations for easy debugging and monitoring  

### Frontend (Streamlit)

- User-friendly tabbed interface for entering expenses and viewing analytics  
- Supports up to 5 expense entries per day, with pre-filled data if available  
- Displays interactive charts for a clear overview of spending habits  

---

## Testing

Automated backend tests ensure your expense data is handled correctly and the app runs reliably.

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mrunali12pots/Python_Web_Development.git
   cd Project_expense_management

2. **Install dependencies:**
   ```bash
   pip install requirements.txt
   
3. **Run The Fast API Server**
   ```bash
   unicorn server.server:app --reload
   
4. **Run Streamlit App**
   ```bash
   streamlit run .\app.py
