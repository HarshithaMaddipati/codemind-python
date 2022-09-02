l,r,k=map(int,input().split())
s=0
for i in range(l,r+1):
    if i%k==0:
        s+=1
print(s)        