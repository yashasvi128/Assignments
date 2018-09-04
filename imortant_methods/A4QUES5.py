import copy
lst = [1, 2, 3, 4, [5, 6], 7]
lst1 = copy.deepcopy(lst)
lst1[4][1] = 2829
print(lst1)
print(lst)
print("The difference between deepcopy and shallow copy is that; in deep copy any changes made to a copy of object do "
      "not reflect in the original object; whereas in any changes made to a copy of object do reflect in the original "
      "object. ")