import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY")

def predict_category(description):
    prompt = f"""
    You are a financial assistant. Categorize this expense into one of:
    ['Food', 'Transportation', 'Entertainment', 'Utilities', 'Shopping', 'Others'].

    Expense: "{description}"
    Just return the category name.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()

csv_file = "expense_data_1.csv"
if os.path.exists(csv_file):
    data = pd.read_csv(csv_file)
else:
    data = pd.DataFrame(columns=["Date", "Description", "Amount", "Category"])

st.title("Smart Expense Tracker")

with st.form("expense_form"):
    date = st.date_input("Date")
    description = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")

    predicted_category = ""
    if description:
        predicted_category = predict_category(description)

    category = st.text_input(
        "Category (auto-predicted, but you can edit)", 
        value=predicted_category
    )

    submitted = st.form_submit_button("Add Expense")

    if submitted:
        new_expense = {"Date": date, "Description": description, "Amount": amount, "Category": category}
        data = pd.concat([data, pd.DataFrame([new_expense])], ignore_index=True)
        data.to_csv(csv_file, index=False)
        st.success(f"Added: {description} - {amount} ({category})")

st.subheader("All Expenses")
st.dataframe(data)

if not data.empty:
    st.subheader("Expense Breakdown by Category")

    category_totals = data.groupby("Category")["Amount"].sum()

    # Bar Chart
    fig, ax = plt.subplots()
    category_totals.plot(kind="bar", ax=ax)
    ax.set_ylabel("Amount")
    st.pyplot(fig)

    # Pie Chart
    st.subheader("Category Distribution")
    fig2, ax2 = plt.subplots()
    category_totals.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
    st.pyplot(fig2)