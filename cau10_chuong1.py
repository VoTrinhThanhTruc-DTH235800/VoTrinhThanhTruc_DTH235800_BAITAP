than_cay = [1, 3, 7, 3, 5, 11]

for sao in than_cay:
    max_dai = max(than_cay)
    spaces = (max_dai - sao) // 2  # Dùng phép chia nguyenexi
    print(" " * spaces + "*" * sao)

for _ in range(2):
    spaces = (max_dai - 3) // 2  # Thay đổi thành 3 để tính đúng
    print(" " * spaces + "* *")