done = False 
n, m = 0, 100
while not done and n!=m:
    n = int(input("Nhap n:"))
    if n < 0:
        done = True
    print("n = ", n)
# dùng break
n, m= 0, 100
while n!=m:
    n = int(input("Nhap n: "))
    if n < 0:
        break
    print("n = ",n)