"""
Create a new list named first_only that contains the first element in each sub-list of nested_lists.
"""


nested_lists = [[4, 8], [16, 15], [23, 42]]

first_only = [item1 for (item1,item2) in nested_lists]

