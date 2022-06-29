n=int(input())
r=0
re=n
n=abs(n)
while n>0:
    d=n%10
    r=r*10+d
    n=n//10
if re>0:
    print(r)
else:
    print(-1*r)