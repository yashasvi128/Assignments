lst = []
for i in range(1,101):
    for n in range(2,i):
        if(i%2==0):
            break
        else:
            lst.append(i)
            break
print(lst)