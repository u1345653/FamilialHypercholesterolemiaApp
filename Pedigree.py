# Creation of Class for Family Pedigree
from Person import Grandparent_1, Grandparent_2, Parent_1, Parent_2, Sibling_1, Sibling_2, Child_1, Child_2, Child_3
import pandas as pd
import numpy as np
import time
numOfRows = 9


grandarray = np.array( [ [Grandparent_1.__dict__]
                       , [Grandparent_2.__dict__]
                       , [Parent_1.__dict__]
                       , [Parent_2.__dict__]
                       , [Sibling_1.__dict__]
                       , [Sibling_2.__dict__]
                       , [Child_1.__dict__]
                       , [Child_2.__dict__]
                       , [Child_3.__dict__]  ]).tolist()

# Using the List iterator to iterate through created objects
object_list = iter(grandarray)

# Confirming type as 'list_iterator'
# print(type(object_list))

# Printing all objects in list_iterator object
for obj in object_list:
    print(obj)