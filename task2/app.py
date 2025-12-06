import streamlit as st
import pandas as pd
import os
from datetime import datetime
from llm import analyze_review

st.set_page_config(page_title="Fynd AI Assignment", layout="wide")

DATA_FILE = "data.csv"

# Create CSV if not exists
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=[
        "timestamp", "rating", "review", "ai_output"
    ]).to_csv(DATA_FILE, index=False)

page = st.sidebar.selectbox("Select Page", ["User Dashboard", "Admin Dashboard"])

# ---------------- USER DASHBOARD ----------------
if page == "User Dashboard":
    st.title("🧾 User Feedback Form")

    rating = st.slider("Select Rating", 1, 5, 5)
    review = st.text_area("Write your review")

    if st.button("Submit"):
        if review.strip() == "":
            st.warning("Please enter a review.")
        else:
            ai_output = analyze_review(review, rating)

            df = pd.read_csv(DATA_FILE)
            new_row = {
                "timestamp": datetime.now(),
                "rating": rating,
                "review": review,
                "ai_output": ai_output
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)

            st.success("Thank you for your feedback!")
            st.subheader("AI Response")
            st.text(ai_output)

# ---------------- ADMIN DASHBOARD ----------------
if page == "Admin Dashboard":
    st.title("📊 Admin Dashboard")

    df = pd.read_csv(DATA_FILE)
    st.dataframe(df)

    st.caption("Showing all user feedback with AI-generated insights.")
