#check if its prime number
def prime(n):
    flag=False
    if n>1:
        for i in range(2,n//2 +1):
            if n%i==0:
                flag=True
    if flag:
        return "Not prime"
    else:
        return "prime"
    
print(prime(4))


#using for-else
def prime(n):
    if n>1:
        for i in range(2, n//2 +1):
            if n%i==0:
                print("not prime")
                break
        else:
            print("prime")
    else:
        print("not prime")


#find prime numbers between given interval

def prime(start,end):
    for i in range(start, end):
        if i>1:
            for j in range(2,i//2 +1):
                if i%j ==0:
                    break
            else:
                print(i)