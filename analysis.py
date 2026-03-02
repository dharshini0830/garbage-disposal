import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your Excel file
df = pd.read_excel("Book1.xlsx", sheet_name="Sheet1")  # Replace with your actual file name

# Rename columns for easier access
df.rename(columns={'Organic (bags)': 'Organic_bags', 'Inorganic(bags)': 'Inorganic_bags', 'Recyclable(bags)': 'Recyclable_bags'}, inplace=True)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Group by date and sum waste types
daily_totals = df.groupby('Date')[['Organic_bags', 'Inorganic_bags', 'Recyclable_bags']].sum().reset_index()

# Plot line chart
plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_totals, x='Date', y='Organic_bags', label='Organic Waste')
sns.lineplot(data=daily_totals, x='Date', y='Inorganic_bags', label='Inorganic Waste')
sns.lineplot(data=daily_totals, x='Date', y='Recyclable_bags', label='Recyclable Waste')
plt.title("Daily Waste Trends")
plt.xlabel("Date")
plt.ylabel("Number of Bags")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()