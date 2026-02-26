import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = r"C:\Users\chaima\Desktop\Data Analysis\week5_project\store.csv"
df_raw = pd.read_csv(path)

print(df_raw.shape)
print(df_raw.head())
print(df_raw.info())
print (df_raw.isnull().sum())
print(df_raw.duplicated().sum())

df = df_raw.copy()

# DATA CLEANING

#/* Remove duplicates */
df = df.drop_duplicates() 
#/* Convert Order Date and Ship Date to datetime format */
df["Order Date"] = pd.to_datetime(
    df_raw["Order Date"],
    format="%d/%m/%Y"
)

df["Ship Date"] = pd.to_datetime(
    df_raw["Ship Date"],
    format="%d/%m/%Y"
)
#/* Convert Postal Code to string and handle missing values */
df["Postal Code"] = df["Postal Code"].astype("Int64").astype(str)
df["Postal Code"] = df["Postal Code"].fillna("UNKNOWN")



# TRANSFORMATION AND FEATURE ENGINEERING

#/* Extract year, month, and quarter from Order Date */
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Order Quarter"] = df["Order Date"].dt.quarter 
# /* Calculate Delivery Delay in days */
df["Delivery Delay"] = (df["Ship Date"] - df["Order Date"]).dt.days
# /* describe the Delivery Delay column */
print(df["Delivery Delay"].describe())
# /* describe the Sales column */
print(df["Sales"].describe())


# KPIs 

#/* Total Sales */
total_sales = df["Sales"].sum()
# /* Sales per Category */
sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
#/* Sales by Region */
sales_by_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
#/* Sales by Segment */
sales_by_segment = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
# /* top 10 products by sales */
top_10_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
# /* mpnthly sales and growth percentage */
monthly_sales = (
    df.groupby(["Order Year", "Order Month"])["Sales"]
    .sum()
    .reset_index()
    .sort_values(["Order Year", "Order Month"])
)

monthly_sales["Growth %"] = monthly_sales["Sales"].pct_change() * 100


# VISUALIZATION

#/* Sales by Category */
sales_by_category.plot(kind="barh")
plt.title("Ventes par catégorie")
plt.xlabel("Sales")
plt.show()

#/* Sales by Region */
sales_by_region.plot(kind="barh")
plt.title("Ventes par région")
plt.xlabel("Sales")
plt.show()

#/* Monthly sales trend */
plt.plot(monthly_sales["Sales"])
plt.title("Tendance mensuelle des ventes")
plt.xlabel("Mois")
plt.ylabel("Sales")
plt.show()

#/* Distribution of Sales */
df["Sales"].plot(kind="hist", bins=30)
plt.title("Distribution des ventes")
plt.xlabel("Sales")
plt.show()

# EXPORTING THE CLEANED DATA

df.to_csv("superstore_clean.csv", index=False)