# -*- coding: UTF-8 -*-
import pandas as pd
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


