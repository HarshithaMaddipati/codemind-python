n=int(input())
s=str(n)
num=list(s)
if(len(set(num))==len(num)):
    print("Unique Number")
else:
    print("Not Unique Number")