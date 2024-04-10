#a:10 B:20
a,b=input().split()
a=int(a)
b=int(b)
cnt=a
flag=True
while flag:
    if cnt>=b:
        flag=False
    if cnt%2==0:
        print(cnt,end=" ")
    cnt= cnt+1