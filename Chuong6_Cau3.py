#from mmap import MAP_TRANSLATED_ALLOW_EXECUTE
from random import randrange

def TaoMatran(m,n):
    D=[]
    for i in range(m):
        dong=[]
        for j in range(n):
            dong.append(randrange(100))
        D.append(dong)
    return D

def InMatran(D):
    for dong in D:
        for element in dong:
            print(f"{element}", end="\t")
        print()

def LayDong(r):
    R=D[r]
    return R

def xuatList1Chieu(L):
    for element in L:
        print(f"{element}", end="\t")


def LayCot(c):
    C=[]
    for i in range(len(D)):
        C.append(D[i][c])
    return C

def Max(D):
    max=D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if D[i][j]>max:
                max=D[i][j]
    return max

m = int(input("Nhap so dong cua ma tran: "))
n = int(input("Nhap so cot cua ma tran: "))
D=TaoMatran(m,n)
print("Ma tran vua tao la: ")
InMatran(D)
r=int(input("Nhap dong can lay: "))
R=LayDong(r)
xuatList1Chieu(R)
c=int(input("\nNhap cot can lay: "))
C=LayCot(c)
max = Max(D)
print("Gia tri lon nhat trong ma tran la: ",max)
