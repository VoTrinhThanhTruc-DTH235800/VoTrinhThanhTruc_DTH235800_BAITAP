a = 0 
while a <100:
    b=0
    while b<40:
        if(a+b)%2 == 0:
            print('*', end = '')
        b +=1
    print()
    a+=1

#số vòng lập là 100*40 = 4000 vòng mà (a+b)%2 ==0 thì mới in "*" nên có 2000 dấu * 