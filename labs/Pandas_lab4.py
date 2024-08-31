# ILT 9
# 1. Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise.

import pandas as pd

file = pd.read_csv('Pandas_lab4.csv')
df = pd.DataFrame(file)
piv_tab = pd.pivot_table(df,
                             values = ['Sales Amount'],
                             index = ['Region','Manager','SalesMan'],
                             aggfunc={'Sales Amount':'sum'})
print(piv_tab)

# 2. Write a Pandas program to create a Pivot table and find the item wise unit sold.
import pandas as pd

file = pd.read_csv('Pandas_lab4.csv')
df = pd.DataFrame(file)
piv_tab = pd.pivot_table(df, values='Sales Amount', index='Item', columns='Region', aggfunc='sum', fill_value=0)
grouped  = df.groupby('Item')['Units'].sum().reset_index()
print(grouped)

# 3. Write a Pandas program to create a Pivot table and find the region wise, item wise unit sold.
import pandas as pd
df = pd.read_csv('Pandas_lab4.csv')
piv_tab = pd.pivot_table(df, values='Units', index=['Region', 'Item'], aggfunc='sum', fill_value=0)
print("Region, Item-wise Units Sold:")
print(piv_tab)

# 4. Write a Pandas program to create a Pivot table and count the manager wise sale and mean value of sale amount.
import pandas as pd
df = pd.read_csv('Pandas_lab4.csv')
piv_tab = pd.pivot_table(df, values='Sales Amount', index='Manager', aggfunc='sum', fill_value=0)
grouped = df.groupby('Manager')['Sales Amount'].agg(['mean','count']).reset_index()
print(grouped)

# chatgpt Exercise

import pandas as pd

data = {
    'Transaction ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Product': ['Laptop', 'Tablet', 'Laptop', 'Smartphone', 'Tablet', 'Smartphone', 'Laptop', 'Smartwatch', 'Smartwatch', 'Smartphone'],
    'Salesperson': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Charlie', 'Alice', 'Bob', 'Alice', 'Charlie'],
    'Sales Amount': [1200, 800, 1100, 500, 700, 550, 1150, 300, 350, 600]
}
df = pd.DataFrame(data)
pivot_table = pd.pivot_table(df, values='Sales Amount', index='Product', columns='Salesperson', aggfunc='sum', fill_value=0)
total_sales_by_product = df.groupby('Product')['Sales Amount'].sum()
print("Total Sales for Each Product:")
print(total_sales_by_product)
total_sales_by_salesperson = df.groupby('Salesperson')['Sales Amount'].sum()
print("\nTotal Sales for Each Salesperson:")
print(total_sales_by_salesperson)

top_selling_product = total_sales_by_product.idxmax()
top_selling_product_amount = total_sales_by_product.max()
top_salesperson = total_sales_by_salesperson.idxmax()
top_salesperson_amount = total_sales_by_salesperson.max()

print(f"\nTop-Selling Product: {top_selling_product} with Sales Amount ${top_selling_product_amount}")
print(f"Top Salesperson: {top_salesperson} with Sales Amount ${top_salesperson_amount}")
print("\nPivot Table of Sales by Product and Salesperson:")
print(pivot_table)
