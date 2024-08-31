# 1. Write a Pandas program to split the following data frame into groups based on Class and count the number of students in that particular class.Also generate a bar chart based on the result and explain the conclusion.
import pandas as pd
import matplotlib.pyplot as plt
student_data = pd.DataFrame({
'school_code': ['s001','s002','s003','s001','s002','s004'],
'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],
'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill',
'David Parkes'],
'age': [12, 12, 13, 13, 14, 12],
'height': [173, 192, 186, 167, 151, 159],
'weight': [35, 32, 33, 30, 31, 32],
'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
)
print(f"Original data \n{student_data}")
data = student_data.groupby('class')['name'].count()
print(f"Class wise no. of students count is \n{data}")
plt.bar(data.index,data.values)
plt.show()

# 2. Write a Pandas program to split the following dataframe by school code and get mean, min, and max value of age for each school. Also generate a horizontal bar chart based on the result and explain the conclusion.

import pandas as pd
import matplotlib.pyplot  as plt
student_data = pd.DataFrame({
'school_code': ['s001','s002','s003','s001','s002','s004'],
'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill',
'David Parkes'],
'age': [12, 12, 13, 13, 14, 12],
'height': [173, 192, 186, 167, 151, 159],
'weight': [35, 32, 33, 30, 31, 32],
'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
)
print(f"Original DataFrame\n{student_data}")
data_stats = student_data.groupby('school_code')['age'].agg(['mean','max','min'])
print(data_stats)
data_stats.plot(kind = 'barh')
plt.show()

# 3.Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group. Using the following dataset find the mean, min, and max values of purchase amount (purch_amt) group by customer id (customer_id).Also generate a line chart based on the result and explain the conclusion.
import pandas as pd
import matplotlib.pyplot as plt
orders_data = pd.DataFrame({
    'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
    'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,3045.6],
    'ord_date':['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
    'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
    'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
print(f"Original Oredr Dataframe\n{orders_data}")
groups = orders_data.groupby('customer_id')['purch_amt'].agg(['mean','min','max'])
print(groups)
groups.plot(kind='line')
plt.show()

# 4. Write a Pandas program to split the following data frame into groups and calculate monthly purchase amount.Also generate a bar chart based on the result and explain the conclusion.

import pandas as pd 
import matplotlib.pyplot as plt
df = pd.DataFrame({
    'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
    'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,3045.6],
    'ord_date':['05-10-2012','09-10-2012','05-10-2012','08-17-2012','10-09-2012','07-27-2012','10-09-2012','10-10-2012','10-10-2012','06-17-2012','07-08-2012','04-25-2012'],
    'customer_id':[3001,3001,3005,3001,3005,3001,3005,3001,3005,3001,3005,3005],
    'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
prch = df.groupby('ord_date')['purch_amt'].sum()
print(prch)
prch.plot(kind='bar')
plt.xlabel("ord_date")
plt.xticks(rotation = 20)
plt.show()

# chatgpt Exercise

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Customer ID': ['C1', 'C2', 'C3', 'C1', 'C2', 'C4', 'C5', 'C6', 'C1', 'C3'],
    'Visit Date': pd.to_datetime([
        '2023-01-01', '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-03',
        '2023-01-04', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07'
    ]),
    'Product Views': [5, 3, 7, 2, 4, 6, 8, 9, 3, 5],
    'Purchases': [1, 0, 1, 0, 2, 1, 2, 3, 0, 1],
    'Revenue': [50, 0, 70, 0, 90, 60, 80, 100, 0, 70]
}
df = pd.DataFrame(data)
unique_customers = df['Customer ID'].nunique()
print(f"Total number of unique customers: {unique_customers}")
total_visits = df.shape[0]
print(f"Total number of visits: {total_visits}")
average_views_per_visit = df['Product Views'].mean()
print(f"Average number of products viewed per visit: {average_views_per_visit:.2f}")
most_viewed_product = df['Product Views'].max()
print(f"Most viewed product (views count): {most_viewed_product}")

total_revenue = df['Revenue'].sum()
print(f"Total revenue: ${total_revenue}")
daily_visits = df.groupby('Visit Date').size()
plt.figure(figsize=(10, 6))
daily_visits.plot(kind='line', marker='o', title='Daily Visit Trend')
plt.xlabel('Date')
plt.ylabel('Number of Visits')
plt.grid(True)
plt.show()
