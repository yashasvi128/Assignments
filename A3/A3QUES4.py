n = int(input("enter the number of items in the list"))
lst =[]
for i in range(n):
    a = input("enter the number ")
    lst.append(a)
lst.sort()
print(lst)
