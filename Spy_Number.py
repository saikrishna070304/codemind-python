n=int(input())
temp=n
s=0
p=1
while temp>0:
    d=temp%10
    s+=d
    p*=d
    temp=temp//10
if s==p:
    print('Spy Number')
else:
    print('Not Spy Number')