--DROP DATABASE QLHS;
CREATE DATABASE QLHS
ON (
NAME = QLHS_mdf, 
    FILENAME = 'E:\CSDL_HS\QLHS.mdf',  
    SIZE = 15, 
    MAXSIZE = 50, 
    FILEGROWTH = 5
)
LOG ON
(
    NAME = QLSV_log, 
    FILENAME = 'E:\CSDL_HS\QLHS.ldf',  
    SIZE = 15, 
    MAXSIZE = 50, 
    FILEGROWTH = 5
);
USE QLHS;
CREATE TABLE Lop (
    MaLop CHAR(3) PRIMARY KEY,
    TenLop NVARCHAR(20) NOT NULL
);
CREATE TABLE HocSinh (
    MaHS CHAR(4) PRIMARY KEY,
    HoTen NVARCHAR(50) NOT NULL,
    NgaySinh DATE,
    GioiTinh NVARCHAR(5),
    MaLop CHAR(3),
    FOREIGN KEY (MaLop) REFERENCES Lop(MaLop)
);
CREATE TABLE MonHoc (
    MaMon CHAR(3) PRIMARY KEY,
    TenMon NVARCHAR(30) NOT NULL
);
CREATE TABLE Diem (
    MaHS CHAR(4),
    MaMon CHAR(3),
    DiemHK1 FLOAT CHECK (DiemHK1 BETWEEN 0 AND 10),
    DiemHK2 FLOAT CHECK (DiemHK2 BETWEEN 0 AND 10),
    PRIMARY KEY (MaHS, MaMon),
    FOREIGN KEY (MaHS) REFERENCES HocSinh(MaHS),
    FOREIGN KEY (MaMon) REFERENCES MonHoc(MaMon)
);
CREATE TABLE TaiKhoan (
    UserName VARCHAR(10) PRIMARY KEY,       -- Mã người dùng: GV01, CB01, v.v.
    PassWord VARCHAR(20) NOT NULL,          -- Mật khẩu đăng nhập
    PhanQuyen NVARCHAR(20) NOT NULL         -- Quyền: Giáo Viên hoặc Admin
);

-- Bảng Lop
INSERT INTO Lop (MaLop, TenLop) VALUES
('L01', N'10A1'),
('L02', N'10A2');

-- Bảng HocSinh
INSERT INTO HocSinh (MaHS, HoTen, NgaySinh, GioiTinh, MaLop) VALUES
('HS01', N'Võ Bình An', '2008-07-17', N'Nam', 'L01'),
('HS02', N'Trần Linh Chi', '2008-06-22', N'Nam', 'L01'),
('HS03', N'Võ Văn Tần', '2006-09-07', N'Nam', 'L01'),
('HS04', N'Trần Minh Hiếu', '2006-05-16', N'Nam', 'L02'),
('HS05', N'Phạm Thùy Chi', '2007-04-08', N'Nữ', 'L02'),
('HS06', N'Lê Minh An', '2007-10-09', N'Nữ', 'L02'); 

drop table TaiKhoan

-- Bảng MonHoc
INSERT INTO MonHoc (MaMon, TenMon) VALUES
('M01', N'Toán'),
('M02', N'Ngữ văn'),
('M03', N'Tiếng Anh');

-- Bảng Diem
INSERT INTO Diem (MaHS, MaMon, DiemHK1, DiemHK2) VALUES
('HS01', 'M01', 5.2, 6.6),
('HS01', 'M02', 5.9, 6.1),
('HS01', 'M03', 7.3, 5.6),
('HS02', 'M01', 6.7, 7.4),
('HS02', 'M02', 6.1, 7.2),
('HS02', 'M03', 8.5, 8.5),
('HS03', 'M01', 7.6, 7.5),
('HS03', 'M02', 9.5, 7.5),
('HS03', 'M03', 8.1, 9.1),
('HS04', 'M01', 9.3, 6.0),
('HS04', 'M02', 8.3, 5.3),
('HS04', 'M03', 7.8, 9.1),
('HS05', 'M01', 7.7, 8.1),
('HS05', 'M02', 9.8, 9.1),
('HS05', 'M03', 8.4, 7.6),
('HS06', 'M01', 8.6, 6.0),
('HS06', 'M02', 7.2, 8.2),
('HS06', 'M03', 8.1, 5.3);
Select* from monhoc
Select* from taikhoan
Select* from lop
Select* from hocsinh
Select* from diem

INSERT INTO TaiKhoan (UserName, PassWord, PhanQuyen)
VALUES 
('GV01', 'L0101', N'Giáo Viên'),
('GV02', 'L0102', N'Giáo Viên'),
('GV03', 'L0203', N'Giáo Viên'),
('CB01', 'CBQL01', N'Admin');
