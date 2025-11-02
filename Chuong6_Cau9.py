from random import randrange

print("Nhap vao 1 mang so tu nhien")
n = int(input("Nhap so phan tu cua List: "))
lst = []
for i in range (n):
    while True:
        value=int(input(f"Nhap phan tu thu {i+1}: "))
        if value>=0:
            lst.append(value)
            break
        else:
            print("Gia tri khong hop le, vui long nhap lai gia tri so tu nhien")


def ktraSNT(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True



def ktrchanle(num):
    if num % 2 == 0:
        return True
    else:
        return False


print("Mang so tu nhien ban vua nhap la: ", lst)

le = [x for x in lst if not ktrchanle(x)]
chan = [x for x in lst if ktrchanle(x)]
nguyento = [x for x in lst if ktraSNT(x)]
khongnguyento = [x for x in lst if not ktraSNT(x)]

# Xuất kết quả
print(f"\nCac so le trong mang: {le} \nCo {len(le)} so le")
print(f"Cac so chan trong mang: {chan}  \nCo {len(chan)} so chan")
print(f"Cac so nguyen to: {nguyento}")
print(f"Cac so khong phai so nguyen to: {khongnguyento}")
