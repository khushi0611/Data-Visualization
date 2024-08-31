# ILT 7
#1. Write a Pandas program to detect missing values of a given DataFrame.

import pandas as pd
import numpy as np
df = pd.DataFrame({'ord_no':[70001,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
                   'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,3045.6],
                   'ord_date':['2012-10-05','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
                   'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
                   'salesman_id':[5002,5003,5001,np.nan,5002,5001,5001,np.nan,5003,5002,5003,np.nan]})
print("Original Orders DataFrame:\n",df)
missing_values = df.isnull()
print("\nMissing values of the said DataFrame:")
print(missing_values.sum())

# 2. Write a Pandas program to drop the rows where at least one element is missing in a given DataFrame.
 
import pandas as pd
import numpy as np
df = pd.DataFrame({'ord_no':[70001,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
                   'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,3045.6],
                   'ord_date':['2012-10-05','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
                   'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
                   'salesman_id':[5002,5003,5001,np.nan,5002,5001,5001,np.nan,5003,5002,5003,np.nan]})
print("\nOriginal Orders DataFrame:")
print(df)
df = df.dropna()
print("\nDrop the rows where at least one element is missing:")
print(df)

# 3. Write a Pandas program to drop the rows where all elements are missing in a given DataFrame.

import pandas as pd
import numpy as np
df = pd.DataFrame({'ord_no':[np.nan,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
                   'purch_amt':[np.nan,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,3045.6],
                   'ord_date':[np.nan,'2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
                   'customer_id':[np.nan,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001]})
print("\nOriginal Orders Dataframe:\n",df)
df = df.dropna(how='all')
print("\ndrop the rows where all elements are missing:\n",df)

# 4. Write a Pandas program to drop those rows from a given DataFrame in which specific columns have missing values.

import pandas as pd
import numpy as np
df = pd.DataFrame({'ord_no':[np.nan,np.nan,70002,np.nan,np.nan,70005,np.nan,70010,70003,70012,np.nan,np.nan],
                   'purch_amt':[np.nan,270.65,65.26,np.nan,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,np.nan],
                   'ord_date':[np.nan,'2012-09-10',np.nan,np.nan,'2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17',np.nan],
                   'customer_id':[np.nan,3001,3001,np.nan,3002,3001,3001,3004,3003,3002,3001,np.nan]})
print("\nOriginal Orders Dataframe:\n",df)
df = df.dropna(how='all')
df = df.dropna(subset=['ord_no', 'purch_amt'])
print("\nDrop those rows in which specific columns have missing values:")
print(df)

# Chatgpt Exercise

import pandas as pd

data = {
    'Property ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Price': [300000, 450000, None, 500000, 600000, 700000, None, 750000, 800000, 900000],
    'Square Footage': [1500, 2000, 2500, 3000, None, 3500, 4000, 4500, 5000, 5500],
    'Bedrooms': [3, 4, 4, 5, 4, 3, 5, 3, None, 4],
    'Bathrooms': [2, 3, 3, 4, 3, 2, 4, 2, 3, None],
    'Location': ['Downtown', 'Suburbs', 'Downtown', 'Suburbs', 'Downtown', 'Rural', 'Rural', 'Suburbs', 'Rural', 'Downtown']
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)
df_cleaned = df.dropna()
df_cleaned = df_cleaned.drop_duplicates()
df_cleaned.to_csv('cleaned_real_estate_data.csv', index=False)

print("\nCleaned Data:")
print(df_cleaned)
