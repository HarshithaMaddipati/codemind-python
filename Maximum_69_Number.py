n=input()
arr=list(n)
for i in range(4):
    if arr[i]=='6':
        arr[i]='9'
        break
print(''.join(arr))    