from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# Load and prepare data
df = pd.read_excel("Book1.xlsx", sheet_name="Sheet1")

# Rename columns for easier access
df.rename(columns={'Organic (bags)': 'Organic', 'Inorganic(bags)': 'Inorganic', 'Recyclable(bags)': 'Recyclable'}, inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
df['DayOfYear'] = df['Date'].dt.dayofyear

# Add total waste column
df['Total Waste'] = df['Recyclable'] + df['Organic'] + df['Inorganic']

# Prepare features and target
X = df[['DayOfYear']]
y = df['Total Waste']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict tomorrow's waste
next_day = pd.DataFrame([[df['DayOfYear'].max() + 1]], columns=['DayOfYear'])
predicted = model.predict(next_day)
print(f"Predicted total waste for tomorrow: {predicted[0]:.2f} bags")
