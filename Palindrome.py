n=int(input())
rev=0
t=0
t=n
while(n!=0):
    d=n%10
    rev=rev*10+d
    n=n//10
if (t==rev):
    print(True)
else:
    print(False)