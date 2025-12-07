import streamlit as st
import pandas as pd
import os


st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🛠️",
    layout="wide"
)

st.title("🛠️ Admin Dashboard")
st.caption("View and analyze all user feedback")


DATA_FILE = "data.csv"

if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=[
        "user_input",
        "ai_response",
        "rating",
        "feedback",
        "timestamp"
    ])
    df.to_csv(DATA_FILE, index=False)
    

df = pd.read_csv(DATA_FILE)


if df.empty:
    st.warning("No feedback submitted yet.")
    st.stop()


if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.sort_values("timestamp", ascending=False)


col1, col2, col3 = st.columns(3)

col1.metric("Total Feedback", len(df))

if "rating" in df.columns:
    col2.metric("Average Rating", round(df["rating"].mean(), 2))
    col3.metric("Highest Rating", df["rating"].max())

# -------------------------------
# Filters
# -------------------------------
st.subheader("Filters")

if "rating" in df.columns:
    rating_filter = st.selectbox(
        "Filter by Rating",
        options=["All", 1, 2, 3, 4, 5],
        index=0
    )

    if rating_filter != "All":
        df = df[df["rating"] == rating_filter]

# -------------------------------
# Feedback Table
# -------------------------------
st.subheader("All User Feedback")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)


if "rating" in df.columns:
    st.subheader("Rating Distribution")
    st.bar_chart(df["rating"].value_counts().sort_index())


st.caption("Admin dashboard built using Streamlit")
