"""
Create a new list named greater_than that contains True or False depending on whether the corresponding item in list a is greater than the one in list b. 
For example, if the 2nd item in list a is 3, and the 2nd item in list b is 5, the 2nd item in the new list should be False.
"""

a = [30, 42, 10]
b = [15, 16, 17]

zipped = zip(a, b)

greater_than = [item1>item2 for (item1,item2) in zipped]

