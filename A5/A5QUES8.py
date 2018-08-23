n = int(input('enter the number of elements of the list'))
lst = []
for i in range(n):
    l = int(input())
    lst.append(l)
print(lst)
l = [i**2 for i in lst]
print(l)
