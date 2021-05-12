# 한수
# 1~99 -> 비교할 자리 없음 => 한수
# 100~
# ex) 123 -> (3-2) == (2-1) => 한수
#     112 -> (2-1) != (1-1) => 한수 X
# 참고: https://gabii.tistory.com/entry/BaekJoonPython3-%EB%B0%B1%EC%A4%80-1065%EB%B2%88-%ED%95%9C%EC%88%98

n=int(input())

cnt=0
for i in range(1,n+1):
    if i < 100:
        cnt+=1
    else:
        j=list(map(int, str(i)))
        if j[0]-j[1] == j[1]-j[2]:
            cnt+=1
print(cnt)