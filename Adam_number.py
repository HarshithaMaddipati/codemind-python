n=int(input())
sq=n*n
num=0
while n>0:
    rem=n%10
    num=num*10+rem
    n=n//10
square=num*num
rev=0
while square>0:
    r=square%10
    rev=rev*10+r
    square=square//10
if(sq==rev):
    print("True")
else:
    print("False")