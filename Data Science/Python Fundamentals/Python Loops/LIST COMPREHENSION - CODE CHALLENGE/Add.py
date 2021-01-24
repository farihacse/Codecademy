"""
You’ve been given two lists: a list of names and a list of ages. Create a new list named users that contains the string "Name: name, Age: age" for each pair of elements in the original lists. For example, if the 5th item in the names list is "Aiyana" and the 5th item in ages is 42, then the 5th item in the new list should be "Name: Aiyana, Age: 42".

As you did in the previous exercise, concatenate your strings together using +. Make sure to add proper capitalization and spaces.
"""

names = ["Shilah", "Arya", "Kele"]
ages = [14, 9, 35]

users = ["Name: " + str(item1) + ", Age: " + str(item2) for (item1,item2) in zip(names, ages)]

