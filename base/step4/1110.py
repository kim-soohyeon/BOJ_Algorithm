N=num=int(input())

su=-1
cnt=0

while (1):
    if(su==N):
        break
    else:
        left=num//10
        right=num%10
        sum=left+right
        su=right*10+sum%10
        num=su
        cnt+=1

print(cnt)