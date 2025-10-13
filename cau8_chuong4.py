print("Viết chương trình tính log(a)^x")
from math import log
a=float(input("Nhập a: "))
x=float(input("Nhập x: "))
if a<=0 or a==1:
    print("a không hợp lệ") 
elif x<=0:
    print("x không hợp lệ")
else:
    kq= log(x)/log(a)
    print("Kết quả log(",a,")^",x," = ",kq)