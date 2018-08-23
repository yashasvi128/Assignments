def perfect():
    n = 1
    while n <= l:
        divisor = 1
        sum = 0
        while divisor < n:
            if not n % divisor:
                sum = sum + divisor
            divisor = divisor + 1
        if sum == n:
            print("The perfect number is",n)
        n = n + 1

l = 1000
perfect()