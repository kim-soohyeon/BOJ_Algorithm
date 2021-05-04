# 양의 정수 n과 n의 각 자리수를 더하는 함수
def d(n):
    n=n+sum(map(int,str(n)))

    return n

# 생성자가 있는지 확인할 리스트
a=[]

# 생성자 찾기
for i in range(1,10001):
    a.append(d(i))

# 셀프넘버 출력
for i in range(1,10001):
    if i not in a:
        print(i)

