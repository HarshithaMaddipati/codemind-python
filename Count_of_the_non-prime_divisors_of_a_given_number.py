n=int(input())
a=0
for i in range(1,n+1,1):
    if n%i==0:
        b=0
        for j in range(1,i+1,1):
            if i%j==0:
                b+=1
        if b!=2:
            a+=1
print(a)