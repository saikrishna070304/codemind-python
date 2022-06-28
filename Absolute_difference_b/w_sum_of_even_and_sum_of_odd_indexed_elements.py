size=int(input())
even=0
odd=0
a=list(map(int,input().split()))
for i in range(0,size):
    if i%2==0:
        even=even+a[i]
    else:
        odd=odd+a[i]
print(abs(even-odd))
