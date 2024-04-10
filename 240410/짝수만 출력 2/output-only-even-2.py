b,a=input().split()
b=int(b)
a=int(a) 
cnt=b              #a:2 b:18
while True:
    if cnt<a:
        break
    if cnt%2==0:
        print(cnt,end=" ")
    cnt=cnt-1

# a이상 b 이하->내림차순









# for cnt in range(a,b+1):
#       if cnt%2==0:
#          print(cnt)