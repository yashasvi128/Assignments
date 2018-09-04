n = int(input("enter the number of elements in the list "))
lst = []
l = []
for i in range(n):
    a = input("enter an element")
    lst.append(a)
#print(lst)
num = int(input("enter the number you want to search "))
for i in lst:
    if num == i:
        lst.remove(num)
print(l)
