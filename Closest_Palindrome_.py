def pal(n):
    temp=n
    rev=0
    while n>0:
        rev=rev*10+n%10
        n//=10
    if rev==temp:
        return True
    else:
        return False
n=int(input())
i=n+1
j=n-1
while not pal(i) and not pal(j):
    i+=1
    j-=1
if pal(i) and pal(j):
    if abs(i-n)==abs(n-i):
        print(j,i)
    else:
        if abs(i-n)>abs(n-j):
            print(j)
        else:
            print(i)
elif pal(i):
    print(i)
else:
    print(j)
    