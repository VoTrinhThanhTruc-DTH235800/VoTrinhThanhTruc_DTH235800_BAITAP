from math import sqrt

print("Chuong trinh tinh dien tich tam giac")

a=float(input("Nhap do dai canh a: "))
b=float(input("Nhap do dai canh b: "))
c=float(input("Nhap do dai canh c: "))

if a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a:
    print("Tam giac khong hop le")
else:
    cv = a+b+c
    p = cv/2
    dt = sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich tam giac la: ", dt)