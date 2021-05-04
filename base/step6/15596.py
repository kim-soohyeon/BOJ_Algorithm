def solve(a):
    ans = 0
    for i in a:
        ans+=i

    # return sum(a)
    return ans

n=int(input())
a=[]

for _ in range(n):
    a.append(int(input()))

print(solve(a))