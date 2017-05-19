# -*- coding: UTF-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
#import numpy as np

plt.figure(1)
ax1 = plt.subplot(111)
ax1.xaxis.set_major_locator(mdates.DayLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m/%d'))
plt.figure(1).set_size_inches(20,10)

sh_basic = pd.read_csv('../csv/000001.csv', encoding="gb2312").set_index(u"日期")
#sh_basic.set_index(sh_basic[u"日期"])
sh_fiance300 = pd.read_csv('../csv/000914.csv', encoding="gb2312").set_index(u"日期")
#sh_fiance300.set_index(sh_fiance300[u"日期"])
#print sh_basic[:3]
dates = [datetime.strptime(date, "%Y/%m/%d").date() for date in sh_fiance300.index]
sh_diff = [sh_fiance300.loc[date, u"收盘价"] -  sh_basic.loc[date, u"收盘价"] for date in sh_fiance300.index]    
plt.sca(ax1)
plt.xticks(pd.date_range(dates[-1], dates[0], freq='12M'))
plt.plot(dates, sh_diff)

#图表显示设置
for label in ax1.get_xticklabels():
    label.set_rotation(30)
    label.set_horizontalalignment('right')
    
for i in [0,1000, 2000, 3000, 4000]:
    plt.plot(dates, [i for x in dates])

#plt.figtext(0.1, 0.92, u'300信息--', color='green')
#plt.figtext(0.15, 0.92, u'300金融--', color='blue')
#plt.figtext(0.2, 0.92, u'上证指数--', color='red')

#sh_data.describe()
plt.show()

