import pandas as pd

df = pd.read_csv("Expense_data_1.csv")
print(df.head())

# CLEAN THE DATA

data = df[["Date", "Category", "Note", "Amount", "Income/Expense"]]
print(data.head())