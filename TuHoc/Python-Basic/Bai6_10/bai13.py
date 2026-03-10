n = int(input("Nhập vào số nguyên n: "))

nam = n//365
n = n%365
tuan = n//7
n = n % 7
ngay = n

print(nam,"nam",tuan,"tuan",ngay,"ngay")
