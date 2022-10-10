# 반복되는 수열 파악하기

n,m,k=map(int,input().split())
index=list(map(int,input().split()))

index.sort()
first_max=index[n-1]
second_max=index[n-2]

# K+1 개가 반복됨
# M//(K+1) 만큼 수열이 반복, M//(K+1)*K 번 큰 수 더해짐
# M%(K+1) 만큼 큰 수가 더해짐
# 큰 수 : M//(K+1)*K + M%(K+1)
# 작은 수 : M//(K+1)

result=(m//(k+1)*k + m%(k+1))*first_max + m//(k+1)*second_max
print(result)