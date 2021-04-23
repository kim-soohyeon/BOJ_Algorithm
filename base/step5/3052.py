a=[]
for _ in range(10):
    n=int(input())
    a.append(n%42)

# 집합 함수 set: 교집합
a=set(a)
print(len(a))
