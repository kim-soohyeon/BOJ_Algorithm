t= int(input()) #테스트 케이스 개수
a=[]
for _ in range(t):
    a.append(list(str(input())))

for i in range(t):
    b = a[i]
    sum = 0
    cnt = 1
    for k in range(len(b)):
        if b[k]=='O':
            sum+=cnt
            cnt += 1
        else:
            cnt=1
    print(sum)