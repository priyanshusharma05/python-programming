n=int(input("enter the number"))
if n==0 and n==1:
    print(n)
else:
    i=2
    a=0
    b=1
    while(i<=n):
        c=a+b
        a=b
        b=c
        i+=1
        print(c)
