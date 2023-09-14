ch=input("enter the character")
l1="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
l2="1234567890"
if ch in l1:
    print("given character is alphabet")
elif ch in l2:
    print("given character is number")
else:
    print("given character is special character")
