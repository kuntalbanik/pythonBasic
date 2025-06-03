#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

#
# Compound interest calculation using while loop
#

# import my custom fuction
from function.functions import area

# import sys


principal: float = 1000
rate: float = 0.05
years = 5
year = 1

while year <= years:
    principal = principal * (1 + rate)
    print(year, principal)
    year += 1


print(area(25))

# string
new_string = "Hello World!"
print(new_string[::-1])
print(new_string.split(" "))

# First class object
#
items = {"number": 42, "text": "Hello"}

print(items["number"])

#
# List comprehension
#
# Rules
# new_list = [যা_রাখবো for উপাদান in উৎস if শর্ত]
# [expression for item in iterable if condition]
#
# 🎯 চ্যালেঞ্জ: নিচের কাজগুলো করো List Comprehension দিয়ে:


# ১ থেকে ১০ পর্যন্ত সংখ্যার বর্গের তালিকা তৈরি করো
number_list = [x * x for x in range(1, 11)]
print(number_list)


# একটি স্ট্রিং লিস্ট থেকে শুধু যেগুলোতে ‘a’ আছে, সেগুলো বের করো
string_list = ["amit", "korolo", "kimka", "motton", "chicken", "john", "rock", "chika"]
newstring_list = [str_lst for str_lst in string_list if "a" in str_lst]
print(newstring_list)


# একটি লিস্ট থেকে ডুপ্লিকেট বাদ দিয়ে নতুন লিস্ট বানাও
