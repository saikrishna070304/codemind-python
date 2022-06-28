size=int(input())
a=list(map(int,input().split()))
odd=0
for i in range(0,size):
    if i%2!=0:
        odd+=a[i]
print(odd)
        