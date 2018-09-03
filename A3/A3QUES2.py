#[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]
n = int(input("enter the number of items in the list"))
lst =[]
for i in range(n):
    a = input("enter the element ")
    lst.append(a)
print(lst)
lst1 = ['google', 'apple', 'facebook', 'microsoft', 'tesla']
print(lst + lst1)
