# 1. Visualize the daily temperature changes over time in a city and give your conclusion

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
days = list(range(1, 32))
temperature = np.random.randint(35,50,31)

plt.figure(figsize=(10, 6))
plt.plot(days, temperature, marker='o', linestyle='-', color='b')

plt.title('Daily Temperature Changes in july')
plt.xlabel('Day of the Month')
plt.ylabel('Temperature (°F)')

plt.grid(True)

plt.show()

# 2. Create a line plot to visualize the daily closing prices of a stock over a year and give your conclusion.

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(3)
days = list(range(1, 78))
stock_prices = np.random.randint(100,200,77)

plt.figure(figsize=(12, 6))
plt.plot(days, stock_prices, marker='o', linestyle='-', color='g')

plt.title('Stock Prices Over a year')
plt.xlabel('Day of the year')
plt.ylabel('Stock Price (USD)')

plt.grid(True)

plt.show()


# ChatGPT Exercise
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

dates = ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', 
         '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10']
sales = [150, 200, 170, 250, 300, 230, 190, 220, 210, 275]

date_objects = [mdates.datestr2num(date) for date in dates]

plt.figure(figsize=(10, 6))
plt.plot(date_objects, sales, linestyle='-', marker='o', color='b')

plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()