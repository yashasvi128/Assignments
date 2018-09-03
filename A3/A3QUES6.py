A = [2, 9, 6, 1]
A.sort()
B = [4,7, 3, 5]
B.sort()
C = A + B
C.sort()
print(C)
even = 0
odd = 0
for i in C:
    if(i%2 == 0):
        even = even+1
    else:
        odd = odd+1
print("the number of even elements in the list are",even)
print("the number of odd elements in the list are",odd)