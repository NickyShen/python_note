import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator

df = pd.DataFrame({'Date': pd.date_range('20190101', periods=6),
                   'Name': ['A', 'A', 'C', 'D', 'E', 'F'],
                   'Sales': 100,
                   'Num': [10, 20, 30, 40, 50, 60]})
#按Name计数
res = df[['Name', 'Num']].groupby('Name').count()
print(res)
#       Num
# Name
# A       2
# C       1
# D       1
# E       1
# F       1

fig = plt.figure()
ax = fig.add_subplot(111)
xs = [idx for idx, value in enumerate(res.index)]
ys = res.Num

# X轴用文字 
labels = list(res.index)
def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels[int(tick_val)]
    else:
        return ''

ax.xaxis.set_major_formatter(FuncFormatter(format_fn))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

ax.plot(xs, ys)
plt.show()

