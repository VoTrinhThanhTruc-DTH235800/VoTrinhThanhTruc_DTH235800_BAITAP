day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

# Các tháng có 31 ngày
if month in (1, 3, 5, 7, 8, 10):
    if 1 <= day <= 30:
        print(f"Ngày kế tiếp: {day+1}/{month}/{year}")
    elif day == 31:
        print(f"Ngày kế tiếp: 1/{month+1}/{year}")
    else:
        print("Ngày KHÔNG hợp lệ")
# Tháng 12 (riêng vì qua năm mới)
elif month == 12:
    if 1 <= day <= 30:
        print(f"Ngày kế tiếp: {day+1}/{month}/{year}")
    elif day == 31:
        print(f"Ngày kế tiếp: 1/1/{year+1}")
    else:
        print("Ngày KHÔNG hợp lệ")

# Các tháng có 30 ngày
elif month in (4, 6, 9, 11):
    if 1 <= day <= 29:
        print(f"Ngày kế tiếp: {day+1}/{month}/{year}")
    elif day == 30:
        print(f"Ngày kế tiếp: 1/{month+1}/{year}")
    else:
        print("Ngày KHÔNG hợp lệ")

# Tháng 2 (xét năm nhuận)
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # năm nhuận
        if 1 <= day <= 28:
            print(f"Ngày kế tiếp: {day+1}/{month}/{year}")
        elif day == 29:
            print(f"Ngày kế tiếp: 1/{month+1}/{year}")
        else:
            print("Ngày KHÔNG hợp lệ")
    else:  # năm thường
        if 1 <= day <= 27:
            print(f"Ngày kế tiếp: {day+1}/{month}/{year}")
        elif day == 28:
            print(f"Ngày kế tiếp: 1/{month+1}/{year}")
        else:
            print("Ngày KHÔNG hợp lệ")

else:
    print(f"Tháng {month} KHÔNG hợp lệ")
