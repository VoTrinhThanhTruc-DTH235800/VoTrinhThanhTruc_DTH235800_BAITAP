thang = int(input("Nhap vao 1 thang: "));
if (thang <= 0 or thang > 12):
    print("Nhap thang KHONG hop le")
else:
    if (thang >= 1 and thang <=3):
        print("Tháng", thang, "thuộc quý 1");
    elif (thang >= 4 and thang <= 6):
        print("Tháng", thang, "thuộc quý 2");
    elif (thang >= 7 and thang <=9 ):
        print("Tháng", thang, "thuộc quý 3");
    else:
        print("Tháng", thang, "thuộc quý 4");


