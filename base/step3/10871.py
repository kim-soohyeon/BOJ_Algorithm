N,X=map(int,input().split())
A=list(map(int, input().split()))

lst=[]

for i in range(N):
    if A[i]<X:
       lst.append(A[i])

print(*lst)