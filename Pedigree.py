# Creation of Class for Family Pedigree
from Person import Person
import pandas as pd
import numpy as np
from scipy import stats
import time

# Series of Events:
#  1 - Grab the values associated with objects -- make them 1-dimensional
#  2 - Convert 1-d object-values into Array
#  3 - Convert Array to DF & define desired columns

# Grandparent 1
Grandparent_1 = Person( id = 1
                       , age = 72
                       , gender = "Male"
                       , ldlc = 200
                       , totc = 210
                       , txstatus = 0
                       , cadstatus = 9
                       , cadageonset = 0
                       , dnadx = 9
                       , fhprob = 0 )

# Grandparent 2
Grandparent_2 = Person(id = 2
                       , age = 73
                       , gender = "Female"
                       , ldlc = 190
                       , totc = 150
                       , txstatus = 9
                       , cadstatus = 9
                       , cadageonset = 0
                       , dnadx = 0
                       , fhprob = 0)

# Parent 2
Parent_2 = Person(id = 3
                  , age = 50
                  , gender = "Male"
                  , ldlc = 180
                  , totc = 170
                  , txstatus = 9
                  , cadstatus = 9
                  , cadageonset = 0
                  , dnadx = 9
                  , fhprob = 0)

# Sibling 1 of Parent 1
Sibling_1 = Person(id = 4
                   , age = 42
                   , gender = "Female"
                   , ldlc = 170
                   , totc = 190
                   , txstatus = 0
                   , cadstatus = 0
                   , cadageonset = 0
                   , dnadx = 0
                   , fhprob = 0)

# Sibling 2 of Parent 1
Sibling_2 = Person(id = 5
                   , age = 42
                   , gender = "Male"
                   , ldlc = 185
                   , totc = 199
                   , txstatus = 0
                   , cadstatus = 9
                   , cadageonset = 0
                   , dnadx = 9
                   , fhprob = 0)

# Parent 1
Parent_1 = Person(id = 6
                  , age = 48
                  , gender = "Female"
                  , ldlc = 160
                  , totc = 163
                  , txstatus = 9
                  , cadstatus = 0
                  , cadageonset = 0
                  , dnadx = 9
                  , fhprob = 0)

# Child 1
Child_1 = Person(id = 7
                 , age = 16
                 , gender = "Male"
                 , ldlc = 210
                 , totc = 232
                 , txstatus = 0
                 , cadstatus = 9
                 , cadageonset = 0
                 , dnadx = 9
                 , fhprob = 0)

# Child 2
Child_2 = Person(id = 8
                 , age = 20
                 , gender = "Male"
                 , ldlc = 225
                 , totc = 229
                 , txstatus = 1
                 , cadstatus = 9
                 , cadageonset = 0
                 , dnadx = 9
                 , fhprob = 0)

# Child 3
Child_3 = Person(id = 9
                 , age = 22
                 , gender = "Male"
                 , ldlc = 230
                 , totc = 232
                 , txstatus = 9
                 , cadstatus = 0
                 , cadageonset = 0
                 , dnadx = 0
                 , fhprob = 0)

person_list = [Grandparent_1, Grandparent_2, Parent_2, Sibling_1, Sibling_2, Parent_1, Child_1, Child_2, Child_3]

object_list = iter(person_list)

# print(object_list)

for obj in object_list:
    a = np.array([np.append(key, value) for key, value in obj.__dict__.items()])
    # print(a.shape)


print(type(a))
print(a)
print()
print(type(a[1]))
print(a[1])















### Appendix

# Function to
#
#
# vallist = []
# for attr, value in grandarray.__dict__.items():
#     vallist.append(value)
#
# print(vallist)

# Using the List iterator to iterate through created objects
# object_list = iter(grandarray)

# # Printing all objects in list_iterator object
# for obj in object_list:
#     print(obj)

# df = pd.DataFrame(object_list, columns=['id', 'pedigree_role', 'age', 'gender', 'ldlc', 'totc', 'txstatus', 'cadstatus', 'cadageonset', 'dxdnastatus', 'fhprob', 'ldlcfh', 'ldlcnotfh', 'txfh', 'txnotfh', 'cadfh', 'cadnotfh'])
# print(df.values)

# print(df)