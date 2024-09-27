# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: September 27th, 2024
# Purpose: Practice adding and removing elements in list.
# Usage: ./lab3g.py

# Follow the specific instructions given in the README.md file

mylist = [1,2,3,4,5,6]
mylist.append(7)
mylist.insert(0,0)
mylist.pop(2)
print(mylist)
print("The element 6 is present at the index",mylist.index(6))