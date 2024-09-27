# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: September 27th, 2024
# Purpose: Practice writing a for loop with range function and process numbers inside the loop.
# Usage: ./lab3e.py

# Follow the specific instructions given in the README.md file

num1 = input("Enter a number you would like to see the multiplaction table from 1 to 10: ")
while num1.isdigit() == False:
    num1 = input("Enter a number you would like to see the multiplaction table from 1 to 10: ")
num1 = int(num1)

for i in range(1,11):
    print(num1,"X",i,"=",num1*i)