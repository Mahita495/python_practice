def fibo_rec(n):
    if n==0 or n==1:
        return n
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)
n=10
if n<=0:
    print("Invalid")
else:
    for i in range(n):
        print(fibo_rec(i))