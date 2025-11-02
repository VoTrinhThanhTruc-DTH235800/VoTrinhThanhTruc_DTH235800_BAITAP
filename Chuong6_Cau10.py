# Hàm nhập ma trận
def nhapMaTran(m, n, ten="MaTran"):
    print(f"Nhập các phần tử cho {ten} ({m}x{n}):")
    M = []
    for i in range(m):
        dong = []
        for j in range(n):
            x = int(input(f"{ten}[{i}][{j}] = "))
            dong.append(x)
        M.append(dong)
    return M

# Hàm in ma trận
def inMaTran(M):
    for dong in M:
        for element in dong:
            print(f"{element:4}", end=" ")
        print()

# Hàm cộng 2 ma trận
def congMaTran(A, B):
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        dong = []
        for j in range(n):
            dong.append(A[i][j] + B[i][j])
        C.append(dong)
    return C

# Hàm chuyển vị ma trận
def chuyenVi(M):
    m = len(M)
    n = len(M[0])
    C = []
    for j in range(n):
        dong = []
        for i in range(m):
            dong.append(M[i][j])
        C.append(dong)
    return C

# --- Chương trình chính ---
m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

A = nhapMaTran(m, n, "A")
B = nhapMaTran(m, n, "B")

print("\nMa trận A:")
inMaTran(A)
print("\nMa trận B:")
inMaTran(B)

# Cộng 2 ma trận
C = congMaTran(A, B)
print("\nMa trận C = A + B:")
inMaTran(C)

# Tính chuyển vị
print("\nChuyển vị ma trận A:")
inMaTran(chuyenVi(A))
print("\nChuyển vị ma trận B:")
inMaTran(chuyenVi(B))
