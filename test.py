#!/usr/bin/env python3
# encoding: utf-8

"""
@author: Rita
@software: XXX
@file: test.py
@time: 2020/8/31 14:26
@desc:

"""

import random

# print(random.randrange(0, 100, 2))
list1 = random.shuffle([1, 2, 3, 4, 5, 6])

list2 = random.choice([1, 2, 3])
print(list2)
print(list1)
