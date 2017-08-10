#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename='sitka_weather_07-2014.csv'
with open(filename) as f:
	reader=csv.reader(f)
	header_row=next(reader)
      #从文件中获取最高温度
	dates,highs,lows=[],[],[]
	for row in reader:
		#highs.append(row[1])
		current_date=datetime.strptime(row[0],"%Y-%m-%d")
		dates.append(current_date)

		high=int(row[1])
		highs.append(high)

		low=int(row[3])
		lows.append(low)

	#print(highs)
	#print(lows)

fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)            #alpha制定颜色的透明度,0完全透明
plt.plot(dates,lows,c='yellow',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

plt.title("Daily high and low temperatures,JUly 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()
	#print(header_row)
	#for index,column_header in enumerate(header_row):     #获取每个元素的索引及其值
	#	print(index,column_header)