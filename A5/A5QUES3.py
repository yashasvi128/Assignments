a = int(input("enter your age"))
b = int(input("enter your age"))
c = int(input("enter your age"))
if (a > b and a > c):
    print('the oldest is {}'.format(a))
elif (b > a and b > c):
    print('the oldest is {}'.format(b))
elif (c > a and c > b):
    print('the oldest is {}'.format(c))
if (a < b and a < c):
    print('the youngest is {}'.format(a))
elif (b < a and b < c):
    print('the youngest is {}'.format(b))
elif (c < a and c < b):
    print('the youngest is {}'.format(c))