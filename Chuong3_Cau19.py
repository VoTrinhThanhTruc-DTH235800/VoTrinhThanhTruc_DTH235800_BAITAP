import math

def S(x, n):
    tong = x
    for k in range(1, n + 1):
        mu = 2 * k + 1
        tong += x ** mu / math.factorial(mu)
    return tong

if __name__ == "__main__":
    x = float(input("Nhap x: "))
    n = int(input("Nhap n: "))
    print(f"S({x},{n}) = {S(x, n)}")
