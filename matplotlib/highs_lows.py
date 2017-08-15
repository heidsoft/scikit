#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename='sitka_weather_07-2014.csv'
with open(filename) as f:
	reader=csv.reader(f)
	header_row=next(reader)
      
	dates,highs,lows=[],[],[]      #从文件中获取最高温度,最低温度,日期
	for row in reader:
		current_date=datetime.strptime(row[0],"%Y-%m-%d")
		dates.append(current_date)
		#highs.append(row[1])
		high=int(row[1])
		highs.append(high)

		low=int(row[3])
		lows.append(low)

	#print(dates)
	#print(highs)
	#print(lows)

fig=plt.figure(dpi=128,figsize=(10,6))             #设置绘图窗口的尺寸，figure函数用于指定图表的高度，宽度，分辨率，背景色
plt.plot(dates,highs,c='red',alpha=0.5)            #alpha制定颜色的透明度,0完全透明
plt.plot(dates,lows,c='yellow',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)   #给图表区域着色，接受一个x值系列和两个y之系列，并填充两个y值之间的区域

plt.title("Daily high and low temperatures,JUly 2014",fontsize=24)       #标题
plt.xlabel('',fontsize=16)            #x轴标题
fig.autofmt_xdate()                   #绘制斜的日期标签 
plt.ylabel("Temperature(F)",fontsize=16) #y轴标题
plt.tick_params(axis='both',which='major',labelsize=16)    #设置刻度标记的大小

plt.show()
	#print(header_row)
	#for index,column_header in enumerate(header_row):     #获取每个元素的索引及其值
	#	print(index,column_header)