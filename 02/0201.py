"""数字输出
<string>[N:M]表示一个左闭右开区间[N,M)
编程实现，从键盘输入一个5位数字，分别输出它的个位数和千位数"""
number = input("Input random number>>")
print("个位是{0},千位是{1}".format(number[-1], number[-4]))
