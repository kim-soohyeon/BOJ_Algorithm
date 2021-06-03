# 문제 출처: https://youtu.be/2zjoKjt97vQ

n=int(input("거스름돈을 입력하세요.\n"))
cnt=0

# 큰 단위의 화폐부터 차례로 확인하기
arr=[500,100,50,10]

for coin in arr:
    cnt+=n//coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n%=coin

print(cnt)
