import random
a=random.randint(1,10)

a=int(a)

c=0
while c<100:
    b=input ('enter number')
    b=int(b)

    if a==b:
        print('win')
        break
    elif b>10 or b<1:
        print('error')
    else:

        print('lose')
        c=c+1

 
 

