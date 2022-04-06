"""
# BMI值计算
# 分别输入身高和体重，输出BMI值，并保留1位小数
"""
weight = float(input("You weight(Kg)>>"))
height = float(input("Your height(Meter)>>"))
BMI = weight/(height*height)
print("BMI is {:.1f}".format(BMI))