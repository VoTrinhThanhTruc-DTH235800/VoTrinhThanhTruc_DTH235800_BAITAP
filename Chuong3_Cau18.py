

# Vẽ hình chữ nhật rỗng với chiều cao n
def hcn(n):
    w = n  # Nếu muốn nhập chiều rộng, thay bằng: w = int(input("Nhập chiều rộng: "))
    for i in range(n):
        if i == 0 or i == n - 1:
            print('* ' * w)
        else:
            print('*' + '  ' * (w - 2) + ' *')

def tamgiac(n):
    # Vẽ tam giác góc phải trên của hình chữ nhật (lật ngược lại)
    w = n  # Nếu muốn nhập chiều rộng, thay bằng: w = int(input("Nhập chiều rộng: "))
    for i in range(n):
        print('  ' * (n - i - 1) + '* ' * (i + 1))


def hinh_dac_biet(n):
    # Tam giác trên
    for i in range(n):
        if i == n - 1:
            print('*' * (2 * n - 1))
        else:
            for j in range(2 * n - 1):
                if j == 0 or j == i:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    # Tam giác dưới
    for i in range(1, n):
        for j in range(2 * n - 1):
            if j == 2 * n - 2 or j == n - 1 + i:
                print('*', end='')
            else:
                print(' ', end='')
        print()

    
if __name__ == "__main__":
    n = int(input("Nhap chieu cao cac hinh: "))
    print("Hinh chu nhat:")
    hcn(n)
    print()
    print("Hinh tam giac:")
    tamgiac(n)
    print()
    
    print("Hinh dac biet:")
    hinh_dac_biet(n)

   


            