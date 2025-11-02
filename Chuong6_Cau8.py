
# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử n: "))

# Nhập dãy số
M = []
for i in range(n):
    num = float(input(f"M[{i}] = "))
    M.append(num)

# Sắp xếp giảm dần
M.sort(reverse=True)

# Xuất dãy sau khi sắp xếp
print("\nDãy số sau khi sắp xếp giảm dần:")
for num in M:
    print(num, end="\t")
print()
