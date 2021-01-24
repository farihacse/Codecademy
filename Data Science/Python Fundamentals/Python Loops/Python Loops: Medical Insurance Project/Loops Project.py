"""
Python Loops: Medical Insurance Project
You are interested in analyzing medical insurance cost data efficiently without writing repetitive code.

In this project, you will use your new knowledge of Python loops to iterate through and analyze medical insurance cost data.

Let’s get started!
"""



"""
-----------------------1--------------------------------
First, let’s take a look at the three lists in script.py:

names stores the names of seven individuals.
estimated_insurance_costs stores the estimated medical insurance costs for the individuals.
actual_insurance_costs stores the actual insurance costs paid by the individuals.
We want to calculate the average insurance cost each person paid. We’ll start by adding up all of the insurance costs.

"""

names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]


# 1. Create a variable total_cost and initialize it to 0.

total_cost = 0

# 2. Use a for loop to iterate through actual_insurance_costs and add each insurance cost to the variable total_cost.

for item in actual_insurance_costs:
  total_cost = total_cost + item
  
# 3. After the for loop, create a variable called average_cost that stores the total_cost divided by the length of the actual_insurance_costs list.

average_cost = total_cost/len(actual_insurance_costs)

# 4.  Print average_cost with the following message: Average Insurance Cost: <average_cost> dollars.

print("Average Insurance Cost: " + str(average_cost) + " dollars.")

""" 5. 
For each individual in names, we want to determine whether their insurance cost is above or below average.
Write a for loop with variable i that goes from 0 to len(names).
Note: If you run this loop it will return an error because there is currently no code inside of the loop. We’ll fix this in the next step. 
"""
for i in range(len(names)):

""" 6. 
Inside of the for loop, do the following:
Create a variable name, which stores names[i].
Create a variable insurance_cost, which stores actual_insurance_costs[i].
Print out the insurance cost for each individual, with the following message:
The insurance cost for <name> is <insurance_cost> dollars.
"""

for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]


""" 7.
Click “Save” to see the result.
You should see the insurance costs for each of the seven individuals in names. 
The for loop iterated through the entire list and printed out the insurance cost for each individual.
"""

"""
Output:
Average Insurance Cost: 4400.0 dollars.
The insurance cost for Judith is 1100.0 dollars.
The insurance cost for Abel is 2200.0 dollars.
The insurance cost for Tyson is 3300.0 dollars.
The insurance cost for Martha is 4400.0 dollars.
The insurance cost for Beverley is 5500.0 dollars.
The insurance cost for David is 6600.0 dollars.
The insurance cost for Anabel is 7700.0 dollars.
"""

""" 8.  
Inside of the for loop, use if, elif, else statements after the print statement to check whether the insurance cost is above, 
below, or equal to the average. Print out messages for each case:
a. When insurance_cost is higher than the average, print out the following: The insurance cost for <name> is above average.
b. When insurance_cost is lower than the average, print out the following: The insurance cost for <name> is below average.
c. Otherwise, print out the following: The insurance cost for <name> is equal to the average.
"""

for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")
  if (insurance_cost > average_cost):
    print("The insurance cost for " + name + " is above average.")
  elif (insurance_cost < average_cost):
    print("The insurance cost for " + name + " is below average.")
  else:
     print("The insurance cost for " + name + " is equal to the average.")


# 9. Click “Save” to see the results.
# You should see messages indicating the insurance cost for each of the seven individuals and where their insurance cost stands relative to the average.

"""
The insurance cost for Judith is 1100.0 dollars.
The insurance cost for Judith is below average.
The insurance cost for Abel is 2200.0 dollars.
The insurance cost for Abel is below average.
The insurance cost for Tyson is 3300.0 dollars.
The insurance cost for Tyson is below average.
The insurance cost for Martha is 4400.0 dollars.
The insurance cost for Martha is equal to the average.
The insurance cost for Beverley is 5500.0 dollars.
The insurance cost for Beverley is above average.
The insurance cost for David is 6600.0 dollars.
The insurance cost for David is above average.
The insurance cost for Anabel is 7700.0 dollars.
The insurance cost for Anabel is above average.
"""

""" 10. 
If you look closely at actual_insurance_costs and estimated_insurance_costs, you will notice that each of the actual insurance costs 
are 10% higher than the estimated insurance costs. Using a list comprehension, create a new list called updated_estimated_costs, 
which has each element in estimated_insurance_costs multiplied by 11/10.
"""

updated_estimated_costs = [(item * 11/10) for item in estimated_insurance_costs]


# 11. Print updated_estimated_costs. You should see that the list now looks the same as actual_insurance_costs.

print(updated_estimated_costs)

""" 12.  
Congratulations! In this project, you used Python loops to iterate through and analyze medical insurance cost data.
As a data scientist, you want to be able to easily and efficiently go through data and perform analysis on that data without having to write repetitive code. 
Loops are a great place to start.

If you’d like extra practice with Python loops, here are some suggestions to get you started:

Convert the first for loop in the code to a while loop.
Modify the second for loop so that it also calculates how far above or below the average the estimated insurance cost is.

"""

# Convert the first for loop in the code to a while loop.

total_cost = 0 #reseting the total_cost
item = 0
while item < len(actual_insurance_costs):
  total_cost = total_cost + actual_insurance_costs[item]
  item = item + 1
print(total_cost)

average_cost = total_cost/len(actual_insurance_costs)

# Modify the second for loop

i = 0  # loop counter
while i < len(actual_insurance_costs):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")
  if (insurance_cost > average_cost):
    print("The insurance cost for " + name + " is above average.")
  elif (insurance_cost < average_cost):
    print("The insurance cost for " + name + " is below average.")
  else:
     print("The insurance cost for " + name + " is equal to the average.")
  i = i + 1   # increment counter, otherwise it will become infinite loop


