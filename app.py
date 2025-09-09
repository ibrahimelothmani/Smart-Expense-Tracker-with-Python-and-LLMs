import pandas as pd

df = pd.read_csv("Expense_data_1.csv")
print(df.head())

# CLEAN THE DATA

data = df[["Date", "Category", "Note", "Amount", "Income/Expense"]]
print(data.head())


#  Add Multiple Expenses
def add_expense(date, category, note, amount, exp_type="Expense"):
    global data
    new_entry = {
        "Date": date,
        "Category": category,
        "Note": note,
        "Amount": amount,
        "Income/Expense": exp_type
    }
    data = data.append(new_entry, ignore_index=True)
    print(f" Added: {note} - {amount} ({category})")

add_expense("2025-09-09 19:30", "Food", "Shawarma", 2500, "Expense")
add_expense("2025-09-09 08:00", "Subscriptions", "Netflix Monthly Plan", 4500, "Expense")
add_expense("2025-09-09 14:00", "Entertainment", "Outdoor Games with friends", 7000, "Expense")


# Summarize Expenses by Category
def summarize_expenses(by="Category"):
    summary = data[data["Income/Expense"]=="Expense"].groupby(by)["Amount"].sum()
    return summary.sort_values(ascending=False)
print(summarize_expenses())