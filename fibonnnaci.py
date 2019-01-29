#Program to find the fibonnaci series using recursion:---
def fib(n):
    if a==1:
        return 0;
    elif a==2:
        return 1;
    else:
        return  fib(n-1) +fib(n-2)
n=int(input('enter the number:'))
if n<=0:
    print('please enter a positive number.')
else:
    print('Fibonnci series')
    for i in range (n):
        print(i)
