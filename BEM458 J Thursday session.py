#######################################################################################################################################################
# 
# Name: Sairaj Jadhav
# SID: 740093172
# Exam Date: 27/03/2025
# Module: BEMM458
# Github link for this assignment:https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-sairaj0631
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions
my_list = []

#solution 1
# My SID is 740093172, so the first digit is 7, last digit is 2
# Therefore, I will search only for words associated with keys 7 and 2:
allocated_keys = [7, 2]  # "resolve" and "effort"

# Creating an empty list to store the positions of the words
my_list = []

# I will be Using a for loop to search through each word I have to find
for key in allocated_keys:
    word = key_comments[key]  # Get the word (e.g., "resolve", "effort")
    start = customer_feedback.find(word)  # Find where this word starts in the sentence
    end = start + len(word) - 1  # Calculate where this word ends
    my_list.append((start, end))  # Save these positions as a tuple in the list

print(my_list)

#OUTPUT1
[(129, 135), (114, 119)]
##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here: 74
# Insert last two digits of ID number here: 72

# Write your code for Operating Profit Margin

# Write your code for Revenue per Customer

# Write your code for Customer Churn Rate

# Write your code for Average Order Value

# Call your designed functions here

#solution 2
# Function to calculate Operating Profit Margin
def operating_profit_margin(operating_profit, revenue):
    # Operating Profit Margin helps us understand how efficiently 
    # the company converts revenue into operating profit.
    margin = (operating_profit / revenue) * 100
    return margin

# Function to calculate Revenue per Customer
def revenue_per_customer(total_revenue, number_of_customers):
    # Revenue per Customer shows the average revenue generated 
    # by each individual customer, helpful to measure customer value.
    revenue_customer = total_revenue / number_of_customers
    return revenue_customer

# Function to calculate Customer Churn Rate
def customer_churn_rate(customers_lost, total_customers):
    # Customer Churn Rate indicates the percentage of customers 
    # who stopped doing business with the company, 
    # important for evaluating customer retention.
    churn_rate = (customers_lost / total_customers) * 100
    return churn_rate

# Function to calculate Average Order Value
def average_order_value(total_revenue, total_orders):
    # Average Order Value represents how much, on average, a customer spends per order.
    # It helps assess the effectiveness of marketing strategies and pricing.
    avg_order = total_revenue / total_orders
    return avg_order

# Example usage of functions with SID digits (74 and 72) as inputs:
# (Note: Normally these metrics use realistic financial data, 
# but here we're using SID numbers as sample data.)

# Calculate Operating Profit Margin
operating_profit_margin_result = operating_profit_margin(74, 72)
print(f"Operating Profit Margin: {operating_profit_margin_result:.2f}%")

# Calculate Revenue per Customer
revenue_per_customer_result = revenue_per_customer(74, 72)
print(f"Revenue per Customer: ${revenue_per_customer_result:.2f}")

# Calculate Customer Churn Rate
customer_churn_rate_result = customer_churn_rate(74, 72)
print(f"Customer Churn Rate: {customer_churn_rate_result:.2f}%")

# Calculate Average Order Value
average_order_value_result = average_order_value(74, 72)
print(f"Average Order Value: ${average_order_value_result:.2f}")

#output 2
Operating Profit Margin: 102.78%
Revenue per Customer: $1.03
Customer Churn Rate: 102.78%
Average Order Value: $1.03
##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here

#SOLUTION 3
# Import required libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# Given data from the retail store
price = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

# Reshape the price data for linear regression model (making it 2-dimensional)
price_reshaped = price.reshape(-1, 1)

# Create and fit a linear regression model
regression_model = LinearRegression()
regression_model.fit(price_reshaped, demand)

# To find the price that maximizes revenue:
# Revenue = Price * Demand. Let's check revenue for each price provided.
revenue = price * demand

# Find the index where revenue is maximum
max_revenue_index = np.argmax(revenue)

# Identify the price and revenue at that point
optimal_price = price[max_revenue_index]
max_revenue = revenue[max_revenue_index]

# Now, predict the demand at price £52 using our model
predicted_demand_at_52 = regression_model.predict([[52]])[0]

# Print results clearly
print(f"The price to maximize revenue is £{optimal_price}, with maximum revenue of £{max_revenue}.")
print(f"The predicted demand when the price is set at £52 is approximately {predicted_demand_at_52:.2f} units.")

#OUTPUT 3
The price to maximize revenue is £45, with maximum revenue of £8550.
The predicted demand when the price is set at £52 is approximately 158.17 units.
##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max-value = integer(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.title(Line Chart of 100 Random Numbers)
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()


#solution 4
# Importing necessary libraries
import random
import matplotlib.pyplot as plt

# Asking the user to enter their student ID as the maximum value
max_value = int(input("Enter your Student ID: "))

# Generate 100 random numbers between 1 and the student ID number
random_numbers = [random.randint(1, max_value) for i in range(100)]

# Plotting the random numbers using matplotlib to visualize data clearly
plt.plot(random_numbers, marker='o', markerfacecolor='green', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue')

# Adding title and labels to make the plot understandable
plt.title("Line Chart of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")

# Adding a legend to describe the plotted data
plt.legend()

# Adding gridlines for better readability of the plot
plt.grid(True)

# Displaying the final plotted chart
plt.show()

