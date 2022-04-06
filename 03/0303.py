"""
编写程序，从键盘输入a,b,c的值，计算一元二次方程ax^2+bx+c=0的根
根据b2-4ac的值大于0、等于0及小于0分别进行讨论
"""
a = eval(input("请输入二元一次方程二次项系数"))
b = eval(input("请输入二元一次方程一次项数"))
c = eval(input("请输入二元一次方程常数项"))
deta = b ** 2 - 4 * a * c
m = (-b + (b * b - 4 * a * c)**0.5)/(2 * a)
n = (-b - (b * b - 4 * a * c)**0.5)/(2 * a)
if deta == 0:
    print("方程有两个相等实根，x1=x2=%s"%(m))
elif deta > 0:
    print("方程有两个不同实根，x1=%s,x2=%s"%(m,n))
else:
    m = complex(-b /(2 * a), (-b * b + 4 * a * c)**0.5/(2 * a))
    n = complex(-b /(2 * a), -(-b * b + 4 * a * c)**0.5/(2 * a))
    print("方程有两个不同虚根,x1={},x2={}".format(m,n))