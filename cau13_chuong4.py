def kt_SHH(n):
    tong = 0
    if n<2:
        return False 
    for i in range(1,n):
        if n%i==0:
            tong += i
    return tong == n
def kt_STV(n):
    tong_tv = 0
    if n < 2:
        return False
    for i in range(1,n):
        if n%i==0:
            tong_tv += i
    return tong_tv > n 


n=int(input("Nhap n: "))
if kt_SHH(n):
    print(n,"la so hoan hao")
else:
    print(n,"khong phai la so hoan hao")

if kt_STV(n):
    print(n,"la so thinh vuong")
else:
    print(n,"khong phai la so thinh vuong")