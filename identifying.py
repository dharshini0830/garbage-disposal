import pandas as pd

# Load your Excel file
df = pd.read_excel("Book1.xlsx", sheet_name="Sheet1")  # Replace with your actual file name

# Rename columns for easier access
df.rename(columns={'Organic (bags)': 'Organic', 'Inorganic(bags)': 'Inorganic', 'Recyclable(bags)': 'Recyclable'}, inplace=True)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Add a total waste column
df['Total Waste'] = df['Recyclable'] + df['Organic'] + df['Inorganic']

# Top 5 waste-generating days
top_days = df.groupby('Date')['Total Waste'].sum().sort_values(ascending=False).head(5)
print("Top 5 waste-generating days:")
print(top_days)

# Waste by location
top_locations = df.groupby('Location')['Total Waste'].sum().sort_values(ascending=False)
print("\nWaste by location:")
print(top_locations)