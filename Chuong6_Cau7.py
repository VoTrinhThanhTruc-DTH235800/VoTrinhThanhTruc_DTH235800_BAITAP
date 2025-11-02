from random import randrange
print("Nhap vao 1 day so theo thu tu tang dan, neu nhap sai quy cach thi yeu cau nhap lai")
n = int(input("Nhap so phan tu cua List: "))
lst = []
for i in range (n):
    while True:
        value=int(input(f"Nhap phan tu thu {i+1}: "))
        if i==0 or value>=lst[i-1]:
            lst.append(value)
            break
        else:
            print("Gia tri khong hop le, vui long nhap lai gia tri lon hon gia tri truoc do cua mang")
 
print("Day so ban vua nhap la: ", lst)