size=int(input())
a=list(map(int,input().split()))
even=0
for i in range(0,size):
    if i%2==0:
        even+=a[i]
print(even)
        