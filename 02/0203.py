"""
#统计长度
#编程实现统计任意数的20次幂的值和位数
#例如2的20次幂的值为1048579，位数为7
"""
number = int(input("Input random number>>"))
result = str(pow(number, 20))
print("Result is {0},total digit is {1}".format(result, len(result)))




