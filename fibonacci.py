n=10
#using while loop
def fibo(n):
    n1,n2=0,1
    print(n1)
    count=1
    while count<n:
        print(n2)
        n1,n2=n2, n1+n2
        count+=1

print(fibo(10))



#using for loop
def fibo2(n):
    a,b=0,1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            a,b=b,a+b
            print(b)
print(fibo2(n))


#usinf recursion

