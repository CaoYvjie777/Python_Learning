"""
编写程序，开发一个循环5次计算的小游戏，每次随机产生两个100以内的数字，让用户计算两个数字之和并输入结果
如果计算结果正确则加一分，如果计算结果错误则不加分。如果正确率大于等于80%，则闯关成功
"""
import random
print("Game Start".center(30,'='))
x=[m for m in range(101)]
rightEx=0
for Round in range(5):
    ret = random.sample(x,2)
    print("Please calculate: %d plus %d equals >>:"%tuple(ret))
    res = input()
    if int(res) == ret[0]+ret[1]:
        print("Right")
        rightEx+=1
    else:
        print("Wrong")
if rightEx>=4:
    print("Victory")
else:
    print("Defeat")


