from openai import OpenAI
import pandas as pd
  
client = OpenAI(api_key="YOUR_API_KEY")


df = pd.read_csv("Expense_data_1.csv")
print(df.head())

data = df[["Date", "Category", "Note", "Amount", "Income/Expense"]]
print(data.head())

def auto_categorize(note):
    prompt = f"""
    Categorize this expense note into one of these categories: 
    Food, Transportation, Entertainment, Other.
    Note: {note}
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Other"

data['Category'] = data.apply(
    lambda row: auto_categorize(row['Note']) if pd.isna(row['Category']) else row['Category'],
    axis=1
)

print(data[['Note', 'Category']].head(10))