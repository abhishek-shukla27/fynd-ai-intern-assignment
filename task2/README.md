# Task 2 – AI-Powered Feedback Dashboard (Streamlit)

## Overview
This task implements a simple AI-powered feedback system using **Streamlit**.  
Users can submit feedback through a web interface, receive an AI-generated response, and optionally rate the response. An **admin dashboard** allows viewing and downloading all collected feedback.

The focus of this task is:
- Building a lightweight AI-assisted UI
- Logging user interactions
- Creating an admin view for analysis

---

## Tech Stack
- **Python 3.10+**
- **Streamlit** – UI framework
- **Pandas** – data handling
- **LLM API (Gemini / Placeholder)** – AI responses
- **CSV storage** – simple persistence (`data.csv`)

---

## Folder Structure

task2/
├── app.py # User-facing feedback app
├── admin.py # Admin dashboard
├── data.csv # Stored feedback (auto-created if missing)
├── requirements.txt
└── README.md

---

---

## Features

### User App (`app.py`)
- User submits text feedback
- AI generates a response
- User can rate the response (1–5)
- Feedback + AI response are stored in CSV

### Admin Dashboard (`admin.py`)
- View all collected feedback
- Display data in tabular format
- Download feedback as CSV
- Safe handling when no data is present

---

## Data Storage
All feedback is stored in a local CSV file:


If the file does not exist, it is automatically created with the required columns:
- `user_input`
- `ai_response`
- `rating`
- `feedback`
- `timestamp`

This ensures compatibility with local runs and Streamlit Cloud deployments.

---

## How to Run Locally

1. Install dependencies:
```bash
pip install -r requirements.txt

```
2. Run the user app:
```bash
streamlit run app.py
```
3. Run the admin dashboard (separately):
```bash
streamlit run admin.py
```
## Deployment

-Both app.py and admin.py can be deployed independently on Streamlit Cloud.
-Ensure that data.csv is committed to the repository or auto-created at runtime.

## Notes

-This implementation intentionally uses CSV-based storage for simplicity.

-AI service availability depends on API quota; when unavailable, a fallback message is stored.

-The objective is clarity, robustness, and usability rather than production-scale infrastructure.