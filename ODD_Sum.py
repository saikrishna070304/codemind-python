s=int(input())
a=list(map(int,input().split()))
odd=0
for i in range (0,s):
    if a[i]%2!=0:
        odd+=a[i]
print(odd)