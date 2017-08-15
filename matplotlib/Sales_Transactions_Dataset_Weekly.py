#!/usr/bin/pytthon
# -*- coding:utf-8 -*-

import csv
import matplotlib.pyplot as plt

filename='Sales_Transactions_Dataset_Weekly.csv'
with open(filename) as f:
       reader=csv.reader(f)
       header_row=next(reader)
       #for index,column_header in enumerate(header_row):
       #	print(index,column_header)

       product_code,W0,W1=[],[],[]
       for row in reader:
           product_code.append(row[0])
           x = range(len(product_code))

           w0=int(row[1])
           W0.append(w0)

           w1=int(row[2])
           W1.append(w1)
       
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(x,W0,c='green',alpha=0.5)
plt.plot(x,W1,c='red',alpha=0.5)
plt.xticks(x,product_code, rotation=45)   #plt.xticks()/plt.yticks()设置轴记号,人为设置坐标轴的刻度显示的值
plt.title(" Sales_Transactions of W0 and W1",fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel('number',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()

#http://matplotlib.org/examples/ticks_and_spines/tick_labels_from_values.html