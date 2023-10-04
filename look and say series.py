st = input('enter a string')
reg=''
for z in st:
    count=0
    if z not in reg:
        for i in st:
            if i ==z:
               count+=1
        print(z,count,end=" ")
        reg+=z