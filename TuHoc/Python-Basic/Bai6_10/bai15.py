#1 so tien n mua chai 1 lit va chai 2 lit, in ra so tien nho nhat
n,a,b = map(int ,input().split())
if a <= b/2:
    print(n*a)
else:
    if n % 2==0:
        print(n//2*b)
    else:
        print((n-1)//2*b + a)