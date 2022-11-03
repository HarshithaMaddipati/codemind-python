def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
a=int(input())
c=0
for i in range(1,a):
    for j in range(1,a):
        if prime(i)==1 and prime(j)==1:
            if i*j==a:
                print(i,j)
                c=1
                break
    if c==1:
        break
if c==0:
    print(-1)