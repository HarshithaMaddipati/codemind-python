a=int(input())
b=int(input())
for i in range(a,b+1):
    a=i
    c=0
    while a:
        r=a%10
        if r==0:
            c+=1
        elif i%r!=0:
            c+=1
        a=a//10
    if c==0:
        print(i,end=' ')