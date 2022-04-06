"""上机作业5：日期和时间的输出
"""
from datetime import datetime
now=datetime.now()
print(now)
print(now.strftime('%x'))
print(now.strftime('%X'))
