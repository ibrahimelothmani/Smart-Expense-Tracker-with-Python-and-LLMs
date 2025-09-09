import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("Expense_data_1.csv")
print(df.head())
data = df[["Date", "Category", "Note", "Amount", "Income/Expense"]]
print(data.head())

expense_summary = data[data['Category'] != 'Income'].groupby("Category")["Amount"].sum()

# Pie Chart
plt.figure(figsize=(6,6))
expense_summary.plot.pie(autopct='%1.1f%%', startangle=90, shadow=True)
plt.title("Expenses Breakdown by Category")
plt.ylabel("")
plt.show()

# Bar Chart
plt.figure(figsize=(8,5))
expense_summary.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount Spent")
plt.show()