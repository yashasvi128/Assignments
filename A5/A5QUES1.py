y = int(input("enter a year"))
if (y % 400) == 0:
    if (y% 100) == 0:
        if (y % 4) == 0:
            print('{} is a leap year'.format(y))
else:
    print('{} is not a leap year'.format(y))