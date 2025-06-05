#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

#
# Simple dictionary example
#

# 🔹 Challenge 1: (Basic)
# Create a dictionary with keys "name", "age", and "country" and assign any values to them. Then print the dictionary.

person = {"name": "John", "age": 20, "country": "UAE"}

print(person)
print(person["name"])


# 🔹 Challenge 2: (Basic)
# Access and print the value associated with the "age" key from the following dictionary:
# person = {"name": "Nadia", "age": 25, "city": "Dhaka"}

person = {"name": "Nadia", "age": 25, "city": "Dhaka"}
print(person["age"])


# 🔹 Challenge 3: (Basic)
# Add a new key "email" with any email address to the person dictionary above.

person["email"] = "john@abc.com"
print(person)


# 🔹 Challenge 4: (Medium)
# Write a loop to print all key-value pairs from the following dictionary:
# marks = {"math": 80, "english": 75, "science": 90}

marks = {"math": 80, "english": 75, "science": 90}

for key, val in marks.items():
    print(key, " - ", val)
