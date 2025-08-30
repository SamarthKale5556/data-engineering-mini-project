# -------------------------------
# Retail Sales Analysis (Mini Project)
# -------------------------------

# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load and Clean Data
# -------------------------------

# Load dataset
df = pd.read_csv("retail_sales_25.csv")

# Remove duplicate and missing records
df = df.drop_duplicates()
df = df.dropna()

# Create a new column for total sales value
df["Total_Sales"] = df["Price"] * df["Quantity"]

# -------------------------------
# 2. Basic Business Insights
# -------------------------------

# Total revenue earned
total_revenue = df["Total_Sales"].sum()

# Best selling product (by sales value)
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

# Top customer (who spent the most)
top_customer = df.groupby("Customer")["Total_Sales"].sum().idxmax()

# Revenue by product category
category_sales = df.groupby("Category")["Total_Sales"].sum().reset_index()

# Daily revenue trend
daily_sales = df.groupby("Date")["Total_Sales"].sum().reset_index()

# Prepare summary table
summary = pd.DataFrame({
    "Total Revenue": [total_revenue],
    "Best Selling Product": [best_product],
    "Top Customer": [top_customer]
})

# Print insights
print("===== Retail Sales Insights =====")
print(summary.to_string(index=False))

print("\n===== Revenue by Category =====")
print(category_sales.to_string(index=False))

print("\n===== Daily Sales Trend =====")
print(daily_sales.to_string(index=False))

# -------------------------------
# 3. Visualization Section
# -------------------------------

# Apply a clean theme for charts
sns.set_theme(style="whitegrid", palette="deep")

# --- (A) Sales Trend Over Time ---
# Convert Date column into datetime
df["Date"] = pd.to_datetime(df["Date"])

# Group sales by Date
daily_sales = df.groupby("Date")["Total_Sales"].sum().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=daily_sales, x="Date", y="Total_Sales", marker="o")
plt.title("Daily Sales Trend", fontsize=14, weight="bold")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.close()

# --- (B) Sales by Category ---
plt.figure(figsize=(8, 5))
sns.barplot(data=category_sales, x="Category", y="Total_Sales")
plt.title("Sales by Category", fontsize=14, weight="bold")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
plt.close()

# --- (C) Top 5 Products by Sales ---
top_products = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .reset_index()
    .nlargest(5, "Total_Sales")
)

plt.figure(figsize=(8, 5))
sns.barplot(data=top_products, x="Total_Sales", y="Product")
plt.title("Top 5 Products by Sales", fontsize=14, weight="bold")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.tight_layout()
plt.show()
plt.close()


