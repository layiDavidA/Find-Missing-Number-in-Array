# Find missing number in Array in Python

a = [1, 3, 4, 5, 6, 7, 8]


def missingnum():
    n = a[-1]
    total = n*(n+1)//2
    su = sum(a)
    print(total-su)


missingnum()
