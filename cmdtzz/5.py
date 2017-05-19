# -*- coding: UTF-8 -*-
import pandas as pd
import matplotlib.pyplot as plt 
sh601398 = pd.read_csv('../csv/lrb601398.csv', encoding="gb2312").set_index(u'报告日期')

year = 9999
year_sh601398_profit = pd.DataFrame(columns=['gross_profit', 'net_profit']) 
year_gross_profit = 0
year_net_profit = 0
print sh601398[1:1]

def append_profit(year, gross_profit, net_profit, df_profit):
    df_temp = pd.DataFrame(data = [[gross_profit, net_profit]], columns = ['gross_profit', 'net_profit'],index = [year])
    return df_profit.append(df_temp)

for date in sh601398[1:1]:
    if not date[0:4].isdigit():
        continue
    temp_year = date[0:4]
    if year == temp_year:
        year_gross_profit += int(sh601398.loc[u'利润总额(万元)' , date])
        year_net_profit += int(sh601398.loc[u'净利润(万元)', date])
    else:
        if year != 9999:
            year_sh601398_profit = append_profit(year, year_gross_profit, year_net_profit, year_sh601398_profit)
            #print year_sh601398_profit
        year = temp_year
        year_gross_profit = int(sh601398.loc[u'利润总额(万元)' , date])
        year_net_profit = int(sh601398.loc[u'净利润(万元)', date])
    
year_sh601398_profit = append_profit(year, year_gross_profit, year_net_profit, year_sh601398_profit)
print  year_sh601398_profit 

sh601398_security = pd.read_csv('../csv/601398.csv', encoding="gb2312").set_index(u"日期")

def map_year(date):
    return date[0:4]

series_security = sh601398_security.groupby(map_year)[u'收盘价'].mean()
year_sh601398_security = pd.DataFrame(data=[value for value in series_security.values], index=[series_security.index],
        columns= ['security'])
print year_sh601398_security 

result = year_sh601398_security.join(year_sh601398_profit)
print result


plt.figure(1)
plt.figure(1).set_size_inches(15,7.5)
ax1 = plt.subplot(111)
plt.plot(result.index, result['security'])
plt.plot(result.index, result['gross_profit']/10000000)
plt.plot(result.index, result['net_profit']/10000000)

#图表显示设置
for label in ax1.get_xticklabels():
    label.set_rotation(30)
    label.set_horizontalalignment('right')
    
for i in [0, 2, 4, 6, 8]:
    plt.plot(result.index, [i for x in result.index])

plt.figtext(0.1, 0.92, u'gross_profit', color='green')
plt.figtext(0.25, 0.92, u'security', color='blue')
plt.figtext(0.4, 0.92, u'net_profit', color='red')

plt.show()


