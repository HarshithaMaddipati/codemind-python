def fibonacciSeries(Number):
    if(Number==0):
        return 0
    elif(Number==1):
        return 1
    else:
        return(fibonacciSeries(Number-1)+fibonacciSeries(Number-2))
n=int(input())
for n in range(0,n):
    print(fibonacciSeries(n),end=' ')