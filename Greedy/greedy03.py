# 문제 출처: https://youtu.be/2zjoKjt97vQ

data=input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 0 혹은 1인 경우, 더하기 수행
    num=int(data[i])
    if num<=1 or result<=1:
        result+=num
    else:
        result*=num

print(result)