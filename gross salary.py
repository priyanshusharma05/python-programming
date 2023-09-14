bs=eval(input("enter your  basic salary"))
if bs<=10000:
    print("Gross salary=",bs+ (20/100)*bs + (80/100)*bs)
elif bs<=20000:
    print("Gross salary=",bs+ (25/100)*bs + (90/100)*bs)
else:
    bs>20000
    print("Gross salary=",bs+ (30/100)*bs + (95/100)*bs)
