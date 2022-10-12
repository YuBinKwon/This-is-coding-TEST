# 게임 개발

n,m=map(int,input().split())
x,y,d=map(int,input().split())

game=[]
for i in range(n):
    g=list(map(int,input().split()))
    game.append(g)

game[x][y]=1

# 회전 함수
def left():
    global d
    d-=1
    if d==-1:
        d=3

dir=[(-1,0),(0,1),(1,0),(0,-1)] # 북동남서
count=1
turn_time=0

while True:
    # 왼쪽 회전
    left()
    nx=x+dir[d][0]
    ny=y+dir[d][1]

    if game[nx][ny]==0:
        game[nx][ny]=1
        x=nx
        y=ny
        count+=1
        turn_time=0

    else:
        turn_time+=1
    # 네 방향 모두 감
    if turn_time==4:
        # 뒤로 가기
        nx=x-dir[d][0]
        ny=y-dir[d][1]

        if game[nx][ny]==0:
            x=nx
            y=ny
        else:
            break
        turn_time=0

print(count)

