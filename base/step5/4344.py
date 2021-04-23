c= int(input()) #테스트 케이스 개수
n=[]

for _ in range(c):
    n.append(list(map(int, input().split())))

for i in range(c):
    b=n[i]
    avg=sum(b[1:])/b[0]
    cnt=0
    for score in b[1:]:
        if score>avg:
            cnt+=1
    answer=cnt/b[0]*100
    print('%.3f'%answer+'%')