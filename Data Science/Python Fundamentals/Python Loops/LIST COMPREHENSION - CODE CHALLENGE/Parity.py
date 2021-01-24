""" 
Create a new list named parity that contains a 1 or a 0 for each element of nums. 
For each element, if that element was even, the new list should contain a 0. 
If the element was odd, the new list should contain a 1.
"""

nums = [4, 8, 15, 16, 23, 42]
parity = [x % 2 for x in nums]
