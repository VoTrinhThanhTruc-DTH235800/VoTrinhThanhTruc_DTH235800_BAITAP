def doc_so(n):
    don_vi = ["", "mốt", "hai", "ba", "bốn", "lăm", "sáu", "bảy", "tám", "chín"]
    chu_so = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    if (n < 0) or (n > 99): 
        return "Số không hợp lệ (Chỉ nhận số có 2 chữ số từ 0 đến 99)";
    if n < 10:
        return chu_so[n].capitalize()
    elif n == 10:
        return "Mười"
    elif n < 20:
            return "Mười" + don_vi[n%10]
    else:
        chuc = n // 10;
        dv = n % 10;
        result = chu_so[chuc].capitalize()  + " mươi"
        if dv == 0:
             return result
        else:
            return result + " " + don_vi[dv]

try:
    n = int(input("Nhập một số nguyên n từ 0 đến 99: "))
    print("Cách đọc:", doc_so(n))
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ!")
