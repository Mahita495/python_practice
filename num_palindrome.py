#check if number is a palindrome

def num_palindrome(n):
    temp=n
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10

    if n==rev:
        return True
    else:
        return False

n=123456 
print(num_palindrome(n))