#using for loop
def palindrome(s):
    s.lower()
    n=len(s)
    for i in range(n):
        if s[i]!=s[n-i-1]:
            return False
    else:
        return True
    
s="nitin"
print(palindrome(s))

#using inbuilt fuction
def palindrome(s):
    temp=''.join(reversed(s))
    if temp==s:
        return True
    else:
        return False
s="nitin"
print(palindrome(s))

#using while loop
def palindrome(s):

    n=len(s)
    first,last=0,n-1
    while first<last:
        if s[first]==s[last]:
            first+=1
            last-=1
        else:
            return False
    return True


