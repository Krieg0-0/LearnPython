# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:27:45 2019

@author: 薛
"""

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a+b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a-b

def multiply(a,b):
    print(f"MULTIPLYING {a}*{b}")
    return a*b

def divide(a,b):
    print(f"DIVIDING {a}/{b}")
    return a / b

print("Let's do some math with just function!")

age = add(30,5)
height = subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print('Here is a puzzle.')

what = add(age, subtract(height, multiply(weight, divide(iq,age))))
print("That becomes:",what, 'Can you do it bby hand?')