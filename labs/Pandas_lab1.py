# ILT 6
# 1. Suppose you are a teacher, and you want to analyze the exam scores of your students in a particular subject. You have recorded the scores of your students for a recent exam, and you want to represent this data using a Pandas Series.
import pandas as pd
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]
data = pd.Series(exam_scores,index=students, name= "Exam Scores")
print(data)

# 2. Suppose you want to track and analyze your household expenses for a month.You have recorded the expenses for various categories, such as groceries, utilities, rent,  transportation, and entertainment. You can represent this expense data using a Pandas Series.
import pandas as pd
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]
Monthly_Expenses = pd.Series(expenses,index=categories, name= "Monthly Expenses (USD)")
print(Monthly_Expenses)

# 3.  Suppose you want to track and analyze the monthly energy consumption in your home. You have recorded the monthly energy usage for electricity and gas over a year, and you want to represent this data using Pandas Series.
import pandas as pd
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
'September', 'October', 'November', 'December']
electricity_usage = [350, 320, 310, 330, 340, 370, 380, 360, 350, 330, 320, 330]
gas_usage = [20, 18, 16, 15, 12, 10, 8, 9, 12, 15, 17, 19]
Ele_use = pd.Series(electricity_usage, index=months,name="Electricity Usage (kWh)")
print("\nElectricity Usage:\n",Ele_use)
Gas_use = pd.Series(gas_usage, index=months,name="Gas Usage (therms)")
print("\nGas Usage:\n",Gas_use)

# 4. Suppose you are managing a website and want to analyze the monthly revenue generated from advertising. You have recorded the monthly revenue for the past year, and you want to represent this data using a Pandas Series.
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
'September', 'October', 'November', 'December']
revenue = [5000, 5200, 4800, 5400, 5600, 5800, 6100, 5900, 6200, 6500, 7000, 6900]
Month_Rev = pd.Series(revenue,index=months,name="Monthly Advertising Revenue")
print(Month_Rev)

# ChatGpt Exercise
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Open': [500, 505, 502, 508, 507, 510, 512, 515, 518, 520],
    'Close': [505, 508, 507, 510, 512, 515, 517, 520, 522, 525]
}
stock_data = pd.DataFrame(data)
stock_data['Date'] = pd.to_datetime(stock_data['Date'])
stock_data.set_index('Date', inplace=True)
start_date = '2023-01-03'
end_date = '2023-01-08'
filtered_data = stock_data.loc[start_date:end_date]

plt.figure(figsize=(10, 5))
plt.plot(filtered_data.index, filtered_data['Open'], marker='o', label='Opening Price')
plt.plot(filtered_data.index, filtered_data['Close'], marker='o', label='Closing Price')
plt.title('SBI Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# Suppose you are an investor interested in analyzing the stock prices of a particular company over a year. You have collected daily closing prices for that company's stock, and you want to perform some analysis like Calculate the average daily return,Find the date with the highest closing price and also generate a line chart using Pandas Series. Further, you need to get some inference out of the chart. Create a ChatGPT prompt to generate the code for this scenario. Based on the code generated, ask ChatGPT to give the conclusion/inference.
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': [
        '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05',
        '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10',
        '2023-01-11', '2023-01-12', '2023-01-13', '2023-01-14', '2023-01-15',
        '2023-01-16', '2023-01-17', '2023-01-18', '2023-01-19', '2023-01-20'
    ],
    'Close': [
        100, 102, 101, 104, 107, 110, 108, 109, 112, 115, 113, 117, 116, 120, 
        122, 121, 125, 123, 126, 128
    ]
}

stock_data = pd.DataFrame(data)

stock_data['Date'] = pd.to_datetime(stock_data['Date'])
stock_data.set_index('Date', inplace=True)

stock_data['Daily Return'] = stock_data['Close'].pct_change()
average_daily_return = stock_data['Daily Return'].mean()
print(f"Average Daily Return: {average_daily_return:.4f}")
max_close_date = stock_data['Close'].idxmax()
max_close_price = stock_data['Close'].max()
print(f"Highest Closing Price: {max_close_price} on {max_close_date.date()}")

stock_data['Close'].plot(title='Daily Closing Prices', figsize=(10, 5))
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.show()



# lab 2

# 1. Write a Pandas program to create a dataframe from a dictionary and display it.
import pandas as pd
score={'Math':[78,85,96,80,86],
       'English':[84,94,89,83,86],
       'Hindi':[86,97,96,72,83]
       }
df = pd.DataFrame(score)
print("\n",df)

# 2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine',
                      'James', 'Emily','Michael', 'Matthew', 'Laura', 'Kevin','Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5,
                       np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no',
                         'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
print("\n",df)

# 3. Write a Pandas program to get the first 3 rows of a given DataFrame.

import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia','Dima','Katherine', 
                      'James','Emily','Michael','Matthew','Laura','Kevin','Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5,
                       np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],'qualify': ['yes','no','yes','no','no','yes',
                        'yes','no','no','yes']}
df = pd.DataFrame(exam_data)
print("\nFirst three rows of the data frame:\n",df.head(3))

# 4. Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine',
                      'James', 'Emily','Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],'qualify': ['yes','no','yes','no','no','yes',
                        'yes','no','no','yes']}
df = pd.DataFrame(exam_data)
print("Original Data\n",df)
selected = ['name','score']
print("Select specific columns:\n",df[selected])

# Chatgpt exercise
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Customer Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'Product Name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop', 'Mouse'],
    'Sales Quantity': [1, 3, 2, 1, 2, 1, 1, 2, 1, 4],
    'Price': [1000, 20, 30, 200, 950, 20, 25, 210, 980, 25],
    'Sales Date': pd.to_datetime([
        '2023-01-15', '2023-01-17', '2023-02-01', '2023-03-12', '2023-04-23',
        '2023-05-14', '2023-06-07', '2023-07-21', '2023-08-15', '2023-09-05'
    ])
}

# Create DataFrame

df = pd.DataFrame(data)
df['Total Revenue'] = df['Sales Quantity'] * df['Price']
total_revenue = df['Total Revenue'].sum()
print(f"Total Revenue for the year: ${total_revenue:.2f}")

average_revenue = df['Total Revenue'].mean()
print(f"Average Revenue per Sale: ${average_revenue:.2f}")

best_selling_product = df.groupby('Product Name')['Sales Quantity'].sum().idxmax()
print(f"Best-Selling Product: {best_selling_product}")

date_highest_revenue = df.groupby('Sales Date')['Total Revenue'].sum().idxmax()
print(f"Date with the Highest Total Revenue: {date_highest_revenue.date()}")

plt.figure(figsize=(10,6))
product_sales = df.groupby('Product Name')['Total Revenue'].sum()
plt.subplot(1,2,1)
product_sales.plot(kind='bar', title='Product vs. Total Sales')
plt.xlabel('Product Name')
plt.xticks(rotation = 45)
plt.ylabel('Total Revenue')

date_sales = df.groupby('Sales Date')['Total Revenue'].sum()
plt.subplot(1,2,2)
date_sales.plot(kind='bar', title='Date vs. Total Sales')
plt.xlabel('Sales Date')
plt.xticks(rotation = 45)
plt.ylabel('Total Revenue')

plt.tight_layout()
plt.show()
