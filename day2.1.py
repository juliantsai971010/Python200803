import random
a=random.randint(1,10)

a=int(a)
c=0

 
while c<5:
    b=input ('enter number')
    
    b=int(b)

    if a==b:
        print('win')
        break
    elif b<a:
        print('再大')
    elif b>a:
        print('再小')

    else:

        print('lose')
        
        if c>5:
            break
        c=c+1

 
 
