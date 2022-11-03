n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(1,n-1):
    if a[i-1]%2==0 and a[i+1]%2==0 and a[i]%2!=0:
        count+=1
print(count)