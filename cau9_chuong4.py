import math
def lap(n):
    return 2.0 * math.cos(math.pi / (2**(n+1)))

n = int(input("Nhap n: "))
print("Can bac 2 lap",n,"lan la: ",lap(n))