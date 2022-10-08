def is_disarium(num):
    temp=0
    for i in range(len(str(num))):
        temp+=int(str(num)[i])**(i+1)
    return temp==num    
num=int(input())
print(is_disarium(num))
