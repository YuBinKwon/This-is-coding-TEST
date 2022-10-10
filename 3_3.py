# 숫자 카드 게임

n,m=map(int,input().split())
card=[]
for i in range(n):
    c=input().split()
    for j in range(m):
        c[j]=int(c[j])
    c.sort()
    card.append(c[0])

card.sort()
print(card[n-1])