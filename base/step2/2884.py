H,M=map(int, input().split())
# H시 M분

if M>=45:
    print(H,M-45)
else:
    if H==0:
        print(23,M+15)
    else:
        print(H-1,M+15)