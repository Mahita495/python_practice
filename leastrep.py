#using dict

def leastchar(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    res = min(d, key=d.get)
    return res

s="aaqjhhhheeekklld"
print(leastchar(s))


#use counter from collections
import collections

ch=collections.Counter(s)
res = min(ch, key=ch.get)
print(res)


    
