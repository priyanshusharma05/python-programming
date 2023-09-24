n=int(input("no."))
a=0
b=0
c=n
while n!=0:
    a=n%10
    b=b*10+a
    n=n//10
if c==b:
        print("palindrome")
else:
        print('not a palindrome')
