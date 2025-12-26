import pandas as pd
import matplotlib.pyplot as plt #data visualization
# Create the figure first
plt.figure(figsize=(6, 4))
# Sales data
sales = pd.Series([250, 270, 300, 280], index=['Jan', 'Feb', 'Mar', 'Apr'])
# Plot the sales
sales.plot(kind='bar', color='yellow') #'bar'','pie',bar,etc..
sales.plot(kind='line', marker='o', color='yellow')
sales.plot(kind='pie', autopct='%1.1f%%', colors=['yellow','gold','orange'])
# Add title and labels
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
# Show the plot
plt.show()

#################################################################################################################################

# Visualization Example

import matplotlib.pyplot as plt

df = pd.read_csv('Sales_100.csv')
print(df.head())

# Line Plot: TotalPrice Trend by OrderID
plt.figure(figsize=(10, 5))
plt.plot(df['OrderID'], df['TotalPrice'], marker='o', color='blue')
plt.title('Total Price Trend by OrderID')
plt.xlabel('OrderID')
plt.ylabel('TotalPrice')
plt.grid(True)
plt.show()

# Bar Chart: Total Price Sales by Product
sales_product = df.groupby('Product')['TotalPrice'].sum()
plt.figure(figsize=(8, 5))
plt.bar(sales_product.index, sales_product.values, color='green')
plt.title('Total Price Sales by Product')
plt.ylabel('Total Sales')
plt.show()

#Hist0gram : Quantity Distribution
plt.figure(figsize=(8, 5))
plt.hist(df['Quantity'], bins=5, color='orange', edgecolor ='black')
plt.title('Quantity Distribution')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.show()

#Scatter Plot : 
plt.figure(figsize=(8, 5))
plt.scatter(df['UnitPrice'],df['TotalPrice'], color='red')
plt.title('UnitPrice vs TotalPrice')
plt.xlabel('UnitPrice')
plt.ylabel('TotalPrice')
plt.show()

# Pie Chart : Quantity Distribution
Product_count = df['Product'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(Product_count, labels=Product_count.index, autopct='%1.1f%%', startangle=140)
plt.title('Product Distribution')
plt.show()