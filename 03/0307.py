"""
编写程序，判断一个整数是否为素数
判断整数x是否为素数，最简单的方法就是用2~x-1之间的所有整数逐一去除x
若x能被其中任意一个数整除，则x就不是素数，否则就为素数
"""
end = int(input("Please input your number>>"))
if end == 1 or end == 2:
    print(end, "is sushu")
for num in range(2, end):
    if end % num == 0:
        print(end, "is not sushu")
        break
else:
    print(end, "is sushu")