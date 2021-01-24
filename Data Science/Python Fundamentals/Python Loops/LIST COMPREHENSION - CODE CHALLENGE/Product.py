"""
Create a new list named product that contains the product of each sub-list of nested_lists.
"""

nested_lists = [[4, 8], [15, 16], [23, 42]]

product = [item1 * item2 for (item1, item2) in nested_lists]

