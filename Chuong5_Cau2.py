def toiuuchuoi():
    s2=s 
    s2=s2.strip()
    arr = s2.split(' ')
    s2= " "
    for x in arr:
        word = x
        if len(word.strip())!=0:
            s2+= word.strip() + " "
    return s2.strip()

s = "   Xin    chao   cac   ban   "
print(s,"=>", len(s))
s = toiuuchuoi()
print(s,"=>", len(s))