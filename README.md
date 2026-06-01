# ♻️ Smart Waste Monitoring Using AI

## 📌 Overview

Smart Waste Monitoring Using AI is a machine learning-based waste management system designed to help educational institutions monitor, analyze, and predict waste generation patterns.

The system collects waste data from various locations such as hostels, classrooms, restrooms, canteens, and school grounds, categorizes waste into organic, inorganic, and recyclable types, and provides AI-driven insights for efficient waste management and sustainability planning.

---

## 🎯 Objectives

* Monitor daily waste generation across multiple locations.
* Categorize waste into Organic, Inorganic, and Recyclable types.
* Predict future waste generation using Machine Learning.
* Visualize waste trends through interactive dashboards.
* Provide disposal guidance and sustainability recommendations.
* Support eco-friendly waste management practices.

---

## ✨ Features

### 📊 Waste Trend Analysis

* Daily waste monitoring
* Location-wise waste tracking
* Historical trend visualization

### ♻️ Waste Categorization

* Organic Waste
* Inorganic Waste
* Recyclable Waste

### 🤖 AI-Based Waste Prediction

* Linear Regression model
* Future waste forecasting
* Data-driven planning support

### 📈 Interactive Dashboard

* Streamlit-based web application
* Line charts
* Pie charts
* Bar charts
* Prediction tables

### 📍 Location Analysis

Identifies top waste-generating areas such as:

* Hostels
* Classrooms
* Restrooms
* Canteens
* School Grounds

### 🌱 Disposal Guidance

Provides disposal recommendations for:

* Organic waste
* Inorganic waste
* Recyclable waste

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Plotly

### Framework

* Streamlit

### Development Environment

* VS Code
* Jupyter Notebook

### Data Source

* Excel Dataset (Book1.xlsx)

---

## 🤖 Machine Learning Model

### Algorithm Used

**Linear Regression**

### Purpose

The model analyzes historical waste data and predicts future waste generation based on:

* Day
* Month
* Weekday

This helps institutions plan waste collection and disposal activities efficiently.

---

## 📂 Dataset Information

### Input Columns

| Column            | Description               |
| ----------------- | ------------------------- |
| Date              | Waste collection date     |
| Organic (bags)    | Organic waste quantity    |
| Inorganic (bags)  | Inorganic waste quantity  |
| Recyclable (bags) | Recyclable waste quantity |
| Location          | Waste collection location |

### Derived Feature

```text
Total Waste = Organic + Inorganic + Recyclable
```

---

## 📊 Visualizations

### Daily Waste Trends

Displays changes in waste generation over time using line charts.

### Waste Composition Analysis

Pie chart showing the percentage contribution of:

* Organic Waste
* Inorganic Waste
* Recyclable Waste

### Top Waste-Generating Locations

Bar chart highlighting locations with the highest waste generation.

---

## ♻️ Disposal Guidance

### Organic Waste

Examples:

* Food scraps
* Fruit peels
* Vegetable waste

Disposal:

* Composting
* Biogas generation

### Inorganic Waste

Examples:

* Plastic wrappers
* Styrofoam materials
* Synthetic products

Disposal:

* Safe landfill disposal
* Waste reduction initiatives

### Recyclable Waste

Examples:

* Paper
* Plastic bottles
* Cardboard

Disposal:

* Recycling centers
* Segregation bins

---

## 🚀 How to Run

### Install Dependencies

```bash
pip install pandas scikit-learn matplotlib plotly streamlit openpyxl
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📷 Screenshots

### Dashboard

Add dashboard screenshot here.

### Waste Trend Analysis

Add line chart screenshot here.

### Waste Prediction

Add prediction screenshot here.

### Waste Categorization

Add waste guidance screenshot here.

---

## 🌍 Real-World Applications

### Smart Schools

* Monitor waste levels
* Improve sustainability practices

### Canteens

* Reduce food waste
* Optimize resource usage

### Hostels

* Track daily waste generation
* Improve collection schedules

### Events and Functions

* Real-time waste monitoring
* Efficient cleanup management

---

## 📈 Impact

* Improved environmental awareness
* Better waste segregation
* Data-driven sustainability planning
* Reduced environmental footprint

---

## 🔮 Future Enhancements

* IoT Sensor Integration
* Real-Time Waste Monitoring
* Mobile Application Support
* Random Forest and Neural Network Models
* Multi-School Analytics Dashboard
* Cloud Deployment

---

## 👩‍💻 Author

**Dharshini Mary J**
B.Tech Artificial Intelligence & Data Science

---

## 📜 License

This project is developed for educational and research purposes.
