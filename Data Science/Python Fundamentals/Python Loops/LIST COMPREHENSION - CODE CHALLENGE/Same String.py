"""
Create a new list called is_Jerry, in which an entry at position i is True 
if the entry in names at position i equals "Jerry". The entry should be False otherwise
"""

names = ["Elaine", "George", "Jerry", "Cosmo"]

# Using == sign to compare two strings

is_Jerry = [item == "Jerry" for item in names]




