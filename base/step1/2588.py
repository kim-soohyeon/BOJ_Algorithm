A=int(input())
B=int(input())
# B = list(map(int,list(input())))

m=[]
m.append(B//100)
m.append(B%100//10)
m.append(B%10)

print(A*m[2])
print(A*m[1])
print(A*m[0])
print(A*B)