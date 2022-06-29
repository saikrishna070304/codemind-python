n=int(input())
p=n*n
s=0
while p>0:
    l=p%10
    s+=l
    p=p//10
if s==n:
    print('Neon Number')
else:
    print('Not Neon Number')