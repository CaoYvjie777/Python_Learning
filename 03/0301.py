"""
编写程序，产生两个10以内的随机整数，以第一个随机整数为半径，第二个随机整数为高，计算并输出圆锥体的体积
"""
import math
import random
a = random.randint(1, 10)
b = random.randint(1, 10)
V = math.pi*a*b/3
print("半径为{}，高为{}，体积为{:.2f}".format(a, b, V))