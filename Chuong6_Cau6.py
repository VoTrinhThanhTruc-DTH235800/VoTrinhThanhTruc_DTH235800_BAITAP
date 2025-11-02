from random import randrange
print("Chuoi N so ngau nhien KHONG TRUNG NHAU")
n = int(input("Nhap so phan tu cua List: "))
lst = []
while len(lst) < n:
    num = randrange(-100, 100)
    if num not in lst:
        lst.append(num)
print("Chuoi N so ngau nhien KHONG TRUNG NHAU la: ", lst)