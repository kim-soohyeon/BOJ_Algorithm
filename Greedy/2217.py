N=int(input())
W=[]

for _ in range(N):
    W.append(int(input()))

# 가장 무거운 무게를 들 수 있는 로프부터 내림차순 정렬
W.sort(reverse=True)

for i in range(N):
    W[i]=W[i]*(i+1)

# 최대값
print(max(W))