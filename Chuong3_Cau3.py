from math import sqrt
print("Chuong trinh giai phuong trinh bac 2");
a = float(input("Nhap a: "));
b = float(input("Nhap b: "));
c = float(input("Nhap c: "));

if a == 0:
    if (b==0) and (c==0):
        print("PT co vo so nghiem");
    elif (b==0) and (c!=0):
        print("PT vo nghiem");
    else:
        x = -c/b;
        print("PT bac nhat co nghiem:", x);
else:
    delta = b*b - 4*a*c;
    if (delta < 0 ):
        print("PT vo nghiem");
    elif (delta == 0):
        x = -b/(2*a);
        print("PT co nghiem kep x1 = x2 =", x);
    else:
        x1 = (-b-sqrt(delta))/(2*a);
        x2 = (-b+sqrt(delta))/(2*a);
        print("PT co 2 nghiem phan biet");
        print("x1 =", x1);
        print("x2 =", x2);


