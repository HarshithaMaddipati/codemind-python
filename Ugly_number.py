def isUgly(n):
    if n==1:
        return 1
    if n<=0:
        return 0
    if n%2==0:
        return(isUgly(n//2))
    if n%3==0:
        return(isUgly(n//3))
    if n%5==0:
        return(isUgly(n//5))
    return 0
if __name__=='__main__':
    no=isUgly(int(input()))
    if no==1:
        print("Ugly Number")
    else:
        print("Not Ugly Number")