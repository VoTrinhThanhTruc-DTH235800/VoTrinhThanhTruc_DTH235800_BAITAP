import re

def songuyenam(s):
    # Tìm tất cả các số nguyên âm trong chuỗi
    nums = re.findall(r'-\d+', s)

    if nums:
        print("Các số nguyên âm trong chuỗi là:")
        for num in nums:
            print(num)
    else:
        print("Không có số nguyên âm trong chuỗi.")

# --- Chương trình chính ---
chuoi = input("Nhập chuỗi: ")
songuyenam(chuoi)
