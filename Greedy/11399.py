N=int(input()) #사람의 수

# 각 사람의 인출 시간
P=list(map(int,input().split()))
time=0

# for i in range(N):
#     for j in range(i+1,N,1):
#         if P[i]>P[j]:
#             num=P[i]
#             P[i]=P[j]
#             P[j]=num

P.sort()

for i in range(N):
    for j in range(i+1):
        time+=P[j]

print(time)
