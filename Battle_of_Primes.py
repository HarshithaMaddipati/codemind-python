def prime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True
n=int(input())
m=int(input())
s1=n+m
s=n+m+1
while prime(s)==False:
    s+=1
print(s-s1)