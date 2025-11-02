from random import randrange

print("Chuong trinh xu ly List")
n = int(input("Nhap so phan tu cua List: "))
lst = [0]*n
for i in range (n):
    lst[i]=randrange(-100,100)
print("list ngau nhien la: ", lst)
print("Moi ban them so moi:")
value=int(input())
lst.append(value)
print(lst)
k=int(input("Ban muon dem so nao:"))
dem= lst.count(k)
print("So lan xuat hien cua so ",k," la: ",dem)
def CheckPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

demnt=0;
tongnt=0
for x in lst:
    if CheckPrime(x):
        demnt+=1
        tongnt+=x
print("So luong so nguyen to trong list la: ",demnt)
print("Tong cac so nguyen to trong list la: ",tongnt)
lst.sort()
print("List sau khi sap xep la: ",lst)