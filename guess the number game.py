n=int(input())
i=2
s=0
while i<=n:
    if i%2==0:
        s+=i
        i+=2
    
print("sum of even numbers =",s)
