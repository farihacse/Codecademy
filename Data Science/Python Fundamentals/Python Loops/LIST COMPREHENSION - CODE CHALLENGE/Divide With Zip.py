"""
Use list comprehension and the zip function to create a new list named quotients that divides the elements 
in list b by those in list a . For example, the second item in the new list should be 2.5 from dividing 5.0 by 2.0.
"""

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

zipped = zip(a,b)

quotients = [item2 / item1 for (item1,item2) in zipped]


