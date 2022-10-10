# 큰 수의 법칙

n,m,k=map(int,input().split())
index=list(map(int,input().split()))

index.sort()
first_max=index[n-1]
second_max=index[n-2]

result=0
count=0
while True:
    for i in range(k):
        if count==m:
            break
        result+=first_max
        count+=1
    if count==m:
        break
    result+=second_max
    count+=1

print(result)