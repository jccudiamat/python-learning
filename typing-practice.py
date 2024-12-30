import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'Product': ['A', 'B', 'C', 'D'],
    'Sales_Q1': [100, 200, 150, 300],
    'Sales_Q2': [110, 190, 160, 310],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Add total sales and growth percentage columns
df['Total_Sales'] = df['Sales_Q1'] + df['Sales_Q2']
df['Growth_Percent'] = ((df['Sales_Q2'] - df['Sales_Q1']) / df['Sales_Q1']) * 100

# Group by category and calculate average total sales
category_sales = df.groupby('Category')['Total_Sales'].mean().reset_index()

# Plot the total sales by product
plt.figure(figsize=(8, 5))
plt.bar(df['Product'], df['Total_Sales'], color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

# Print results
print("Original DataFrame:")
print(df)
print("\nCategory-wise Average Total Sales:")
print(category_sales)

# Save results to a CSV file
df.to_csv('sales_analysis.csv', index=False)
print("\nResults saved to sales_analysis.csv")
