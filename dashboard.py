import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "Book1.xlsx"

def load_data(path: str) -> pd.DataFrame:
	if not os.path.exists(path):
		raise FileNotFoundError(f"Data file '{path}' not found in working directory '{os.getcwd()}'.")
	df = pd.read_excel(path)
	df['Date'] = pd.to_datetime(df['Date'])
	df['Total Waste'] = df['Organic (bags)'] + df['Inorganic(bags)'] + df['Recyclable(bags)']
	return df

def main() -> None:
	st.title("School Waste Management Dashboard")

	try:
		df = load_data(DATA_FILE)
	except Exception as exc:
		st.error(f"Unable to load data: {exc}")
		return

	# Line chart
	st.subheader("Daily Waste Trends")
	daily = df.groupby('Date')[['Recyclable(bags)', 'Organic (bags)', 'Inorganic(bags)']].sum()
	st.line_chart(daily)

	# Pie chart
	st.subheader("Total Waste Composition")
	totals = df[['Recyclable(bags)', 'Organic (bags)', 'Inorganic(bags)']].sum()
	fig, ax = plt.subplots()
	ax.pie(totals, labels=totals.index, autopct='%1.1f%%')
	st.pyplot(fig)

	# Top locations
	st.subheader("Top Waste-Generating Locations")
	top_locations = df.groupby('Location')['Total Waste'].sum().sort_values(ascending=False)
	st.bar_chart(top_locations)

if __name__ == "__main__":
	main()
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("Book1.xlsx")
df['Date'] = pd.to_datetime(df['Date'])
df['Total Waste'] = df['Organic (bags)'] + df['Inorganic(bags)'] + df['Recyclable(bags)']

st.title("School Waste Management Dashboard")

# Line chart
st.subheader("Daily Waste Trends")
daily = df.groupby('Date')[['Recyclable(bags)', 'Organic (bags)', 'Inorganic(bags)']].sum()
st.line_chart(daily)

# Pie chart
st.subheader("Total Waste Composition")
totals = df[['Recyclable(bags)', 'Organic (bags)', 'Inorganic(bags)']].sum()
fig, ax = plt.subplots()
ax.pie(totals, labels=totals.index, autopct='%1.1f%%')
st.pyplot(fig)

# Top locations
st.subheader("Top Waste-Generating Locations")
top_locations = df.groupby('Location')['Total Waste'].sum().sort_values(ascending=False)
st.bar_chart(top_locations)
