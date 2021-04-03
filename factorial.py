def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n

print(factorial(3))


def fibonachi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonachi(n-2)+fibonachi(n-1)
    
print(fibonachi(5))


def frog(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return frog(n-1)+frog(n-2)

print(frog(4))


def frog(n):
    if n ==0 or n==1 :
        return 1
    elif n == 2:
        return 2
    total = 0
    for i in [1, 3, 5]:
        if n-i>=0:
            total += frog(n-i)
    return(total)

print(frog(3))


def fun(x,y):
    if x==0:
        return y
    else:
        return fun(x-1,y+x)

print(fun(2,5))    


#find max number in the list by recursion
arr = [34, 23,12, 43, 54,23,1, 4,22 ,5]

def maxi(a):
    if len(a) == 1:
        print(a[0])
    else:
        if a[0]>a[1]:
            a[0], a[1] = a[1], a[0]
            maxi(a[1:])
        else:
            maxi(a[1:])

print(maxi(arr))            


















