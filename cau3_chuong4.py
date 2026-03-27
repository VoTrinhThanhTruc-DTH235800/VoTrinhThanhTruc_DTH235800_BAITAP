def BMI (height, weight):
    return weight / (height ** 2)
def PhanLoai(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif bmi <= 24.9:
        return "Bình thường"
    elif bmi <= 29.9:
        return "Thừa cân"
    else:
        return "Béo phì"
def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Nguy cơ thấp"
    elif bmi <= 24.9:
        return "Nguy cơ trung bình"
    elif bmi <= 29.9:
        return "Nguy cơ cao"
    elif bmi <= 34.9:
        return "Nguy cơ cao"
    elif bmi <= 39.9:
        return "Nguy cơ rất cao"    
    else:
        return "Nguy cơ nguy hiểm"
    
print("Chương trình tính chỉ số BMI")
print("Nhập vào chiều cao: ")
height = float(input())
print("Nhập vào cân nặng: ")
weight = float(input())
bmi = BMI(height, weight)
print("Chỉ số BMI của bạn là: ", bmi)
print("Phân loại: ", PhanLoai(bmi))
print("Nguy cơ bệnh: ", NguyCoBenh(bmi))