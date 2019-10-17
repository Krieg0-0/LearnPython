# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:13:11 2019

@author: 薛
"""

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()