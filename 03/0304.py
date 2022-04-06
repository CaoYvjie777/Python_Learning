"""
#水费计算
#上海市市属供排水服务区域的居民用户水价同步实行阶梯水价制度：
#第一阶梯水量为每户每年0至220立方米(含)，综合水价为3.45元/立方米;
#第二阶梯水量为每户每年220至300立方米(含)，综合水价为4.83元/立方米;
#第三阶梯水量为每户每年300立方米以上的部分，综合水价为5.83元/立方米。
#编写程序，实现输入每户每年的用水量，输出总水费
"""
water = eval(input("请输入每户每年的用水量(立方米)"))
if water >= 0 and water <= 220:
    fee = 3.45 * water
elif water <= 300:
    fee = 3.45 * 220 + (water - 220) * 4.83
else:
    fee = 3.45 * 220 + 4.83 * 80 + (water - 300) * 5.83
print("总水费%s元"%(fee))