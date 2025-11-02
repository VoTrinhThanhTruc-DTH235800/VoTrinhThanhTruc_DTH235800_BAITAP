def CheckDoiXung(s):
    flag = True 
    for i in range (len(s)):
        if s[i] != s[len(s)-1-i]:
            flag = False
            break
    return flag
def main():
    s = input("Nhap chuoi: ")
    if CheckDoiXung(s):
        print("Chuoi doi xung")
    else:
        print("Chuoi khong doi xung")

while True:
    main();
    print("Tiep khong?(c/k):")
    s= input()
    if s =='k' or s =='K':
        break
print("cam on")