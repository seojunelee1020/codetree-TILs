n=int(input())
cnt=0
while True:
    if cnt>=n:
        break
    cnt=cnt+1
    if cnt%3==0:
        print(cnt,end=" ")