n =int(input())
for i in range(n):
    print(" "*(n-1-i) + "*"*(2*i+1))
for i in range(n):
    print(" ",end ="")
    for j in range(1, 2*i+1):
        print("*",end ="")
    print()