t=float(input("enter the time"))
r=5
h=10
v=3.14*r**2*h
fv=t*15
if fv<v:
    print("underflow condition")
    print("remaining height=",(v-fv)/(3.14*r**2))
elif fv>v:
    print("overflow condition")
    OF=fv-v
    print("overflowed volume=",OF)
else:
    print("warning!!Tank is full now")