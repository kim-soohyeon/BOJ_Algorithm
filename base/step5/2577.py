a= int(input())
b=int(input())
c=int(input())

gob=list(str(a*b*c))

for i in range(10):
    print(gob.count(str(i))) # i를 문자열로 바꾼 뒤, count
