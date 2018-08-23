a = int( input("enter the number of items you want to buy, price of each item is 100Rs."))
b = a*100
if b > 1000:
    c = (10*b/100)
    d = b - c
    print('You have to pay a total of {}'.format(d))
else:
    print('You have to pay a total of {}'.format(b))