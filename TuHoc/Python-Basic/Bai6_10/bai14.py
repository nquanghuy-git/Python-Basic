a,b,c,d = map(int,input("Nhập vào 4 số nguyên: ").split())
tb = (a+b+c*2+d*3)/7
if tb>=8:
    print("Gioi")
elif tb>=6.5 and tb<8:
    print("Kha")
elif tb>=5 and tb<6.5:
    print("Trung binh")
else:
    print("Yeu")