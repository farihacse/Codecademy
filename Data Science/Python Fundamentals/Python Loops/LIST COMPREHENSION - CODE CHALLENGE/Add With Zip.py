"""
Use list comprehension and the zip function to create a new list named sums that sums corresponding items in lists a and b. 
For example, the first item in the new list should be 5 from adding 1 and 4 together.
"""

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

zipped = zip(a, b)

sums = [item1 + item2 for (item1, item2) in zipped] 


