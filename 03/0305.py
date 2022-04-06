"""
编写程序，从键盘输入数字n，通过循环计算1~n的乘积
"""
number = int(input("Please input your number>>:"))
Result = 1
for i in range(1, number+1):
    Result *= i
print("Result is %d" % Result)