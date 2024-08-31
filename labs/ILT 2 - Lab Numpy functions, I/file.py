import numpy as np

# 1. Identify days with extreme temperature conditions
# Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
hot_days = np.where(temperatures > 35)[0]
cold_days = np.where(temperatures < 5)[0]
print("Hot days indices:", hot_days)
print("Cold days indices:", cold_days)




# 2. Split data into quarterly reports
# Input: monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
quarterly_sales = np.split(monthly_sales, 4)
print("Quarterly sales:", quarterly_sales)





# 3. Split customer data into two groups
# Input: customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
# last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])
recent_customers = customer_ids[last_purchase_days_ago <= 30]
older_customers = customer_ids[last_purchase_days_ago > 30]
print("Recent customers:", recent_customers)
print("Older customers:", older_customers)




# 4. Combine full-time and part-time employee data
# Input: full_time_employees = np.array([[101, 'John Doe', 'Full-Time', 55000], [102, 'Jane Smith', 'Full-Time', 60000], [103, 'Mike Johnson', 'Full-Time', 52000]])
# part_time_employees = np.array([[201, 'Alice Brown', 'Part-Time', 25000], [202, 'Bob Wilson', 'Part-Time', 28000], [203, 'Emily Davis', 'Part-Time', 22000]])
full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000],
    [103, 'Mike Johnson', 'Full-Time', 52000]
])
part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
])
all_employees = np.vstack((full_time_employees, part_time_employees))
print("All employees:\n", all_employees)




# Assignment 1. Find the mean of every NumPy array in the given list
# Input: list = [np.array([3, 2, 8, 9]), np.array([4, 12, 34, 25, 78]), np.array([23, 12, 67])]
array_list = [np.array([3, 2, 8, 9]), np.array([4, 12, 34, 25, 78]), np.array([23, 12, 67])]
means = [np.mean(arr) for arr in array_list]
print("Means of arrays:", means)




# Assignment 2. Compute the median of the flattened NumPy array
# Input: x_odd = np.array([1, 2, 3, 4, 5, 6, 7])
x_odd = np.array([1, 2, 3, 4, 5, 6, 7])
median = np.median(x_odd)
print("Median of the array:", median)




# Assignment 3. Compute the standard deviation of the NumPy array
# Input: arr = [20, 2, 7, 1, 34]
arr = np.array([20, 2, 7, 1, 34])
std_dev = np.std(arr)
print("Standard deviation of the array:", std_dev)







# Assignment 4. Read data from CSV, calculate average, identify above average, save to new CSV

# 4.1 Read the data from the CSV file into a NumPy array.
house_prices = np.genfromtxt('house_prices.csv', skip_header=1)

# 4.2 Calculate the average of house prices.
average_price = np.mean(house_prices)
print("Average house price:", average_price)

# 4.3 Identify house prices above the average.
above_average_prices = house_prices[house_prices > average_price]
print("House prices above average:", above_average_prices)

# 4.4 Save the list of high prices to a new CSV file.
np.savetxt('high_prices.csv', above_average_prices)
