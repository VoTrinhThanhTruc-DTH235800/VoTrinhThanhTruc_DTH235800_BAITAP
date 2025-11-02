from ast import Num


def CheckPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
s = "5;7;8;-2;8;11;-13;9;10"
arr=s.split(';')
sochan=0
sole=0
soam=0
sont=0
sum=0
for x in arr:
    print(x)
    num = int(x)
    if num < 0:
        soam += 1
    if num % 2 == 0:
        sochan += 1
    if num % 2 == 1:
        sole+=1
    if CheckPrime(num):
        sont+=1
    sum += num
print("So chan:", sochan)
print("So le:", sole)
print("So am:", soam)
print("So nguyen to:", sont)
print("Trung binh = :", sum/len(arr))
