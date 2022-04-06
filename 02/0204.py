"""
某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的
加密规则如下：
每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第三位交换，第二位和第四位交换。
编程实现，输入一个四位数明文，输出密码
"""
result = ''
number = input("Input four digits>>")
for i in number:
    result += str((int(i)+5) % 10)
    print(result)
result = result[2]+result[3]+result[0]+result[1]
print("Encryption result is {0},".format(result))