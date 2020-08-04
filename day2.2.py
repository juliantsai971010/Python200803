import random
bb=random.randint(2,aa-1)
aa=input('enter')
bb=int(bb)

aa=int(aa)


while aa<100:
    if aa%bb==0:
        print('不是質數')
        break
    else:
        print('是質數')



