from random import randrange
while True:
    somay=randrange(1,101)
    solandoan=0
    win=False
    while solandoan<7:
        solandoan+=1
        songuoi=int(input("May doan [1...100], moi ban doan: "))
        print("Ban doan lan thu ", solandoan)
        if somay==songuoi:
            print("Chuc mung ban da doan dung, so may la: ", somay)
            win=True
            break
        if somay>songuoi:
            print("Ban da doan sai, so may > so ban doan")
        elif somay<songuoi:
            print("Ban da doan sai, so may < so ban doan")
    if win == False:
        print("Game over, so may la: ", somay)
    tieptuc=input("Ban co muon choi tiep khong (y/n)? ")
    if tieptuc=="k":
        break
print("Cam on ban da choi game")