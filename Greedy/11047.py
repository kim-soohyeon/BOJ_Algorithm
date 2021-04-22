
N,K=map(int, input().split())
A=[]

for _ in range(N):
    A.append(int(input()))

count=K//A[N-1] # 몫
s=K%A[N-1] # 나머지
for i in range(N-2,-1,-1):
    count+=s//A[i]
    s=K%A[i]
print(count)