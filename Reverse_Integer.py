def reve(num):
    if num>=0:
        return int(str(num)[::-1])
    else:
        return int('-{val}'.format(val=str(num)[1:][::-1]))
n=int(input())
print(reve(n))