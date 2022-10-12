# 왕실의 나이트

in_data=input()

r=int(in_data[1]) # r=1~8
# ord() : 문자->정수
c=int(ord(in_data[0]))-int(ord('a'))+1 # 1~8 로 변환

# 나이트가 이동할 수 있는 방향
step=[(-2,-1),(-2,+1),(+2,-1),(+2,+1),(-1,-2),(+1,-2),(-1,+2),(+1,+2)]

result=0
for dr,dc in step:
    new_r=r+dr
    new_c=c+dc
    if new_r<1 or new_c<1 or new_r>8 or new_c>8:
        continue
    else:
        result+=1

print(result)