n=int(input())
b=len(str(n))
s=n*n
ld=s%pow(10,b)
if ld==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")