n=5
for row in range(0,n):
    for col in range(row):
        print("*", end=" ")
    print(" ")
for row in range(0,n):
    for col in range(row,n):
        print("*",end=" ")
    print(" ")