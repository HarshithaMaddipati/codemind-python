a,b=map(int,input().split())
if((a and b==a+1) or (a==1 and b==10) or (a==10 and b==1) or (a==b+1 and b)):
    print("Yes")
else:
    print("No")