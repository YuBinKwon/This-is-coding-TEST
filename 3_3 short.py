n,m=map(int,input().split())

result=0

for i in range(n):
    c=list(map(int,input().split()))
    min_value=min(c)
    result=max(result,min_value)

print(result)