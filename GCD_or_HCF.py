def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)
  
a,b=map(int,input().split())

  
# prints 12
print (end="")
print (hcfnaive(a,b))