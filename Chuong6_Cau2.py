from random import randrange

print("Chuong trinh xu ly List")
lst=[]
n = int(input("Nhap so phan tu cua List: "))
for i in range (n):
    lst.append(randrange(0,100))
print("list ngau nhien la: ", lst)

x=int(input("Nhap so can them vao list: "))
lst.append(x)
print("List sau khi them la: ",lst)
k=int(input("Moi ban nhap so can xoa:"))
while k in lst:
    lst.remove(k)
print("List sau khi xoa la: ",lst)


def ktraDoixung(lst):
    for i in range(len(lst)):
        if lst[i] != lst[len(lst)-1-i]:
            return False
    return True

kt= ktraDoixung(lst)
if kt:
    print("List doi xung")
else:
    print("List khong doi xung")