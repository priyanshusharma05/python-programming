import random 
m=random.randrange(1,101)
score=10
while True:
    a=int(input("giuess a number b/w 1 and 100"))
    if a==m:
        print("cong.you won with score =",score)
        break
    elif a>m:
        print("large")
    else:
        print("small")
    score-=1