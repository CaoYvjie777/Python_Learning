"""问题
一年365天，以第1天的能力值为基数，记为1.0，当好好学习时能力值相比前一天提高1‰，当没有学习时由于遗忘等原因能力值相比前一天下降1‰。每天努力和每天放任，一年下来的能力值相差多少呢？
"""
dayup = pow((1.0+0.001), 365)
daydown = pow((1.0-0.001), 365)
print("向上：{:.2f},向下:{:.2f}".format(dayup, daydown))
