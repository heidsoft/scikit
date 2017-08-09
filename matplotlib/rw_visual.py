#!/usr/bin/python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
from random_walk import RandomWalk
#只要程序处于活动状态，就不断的模拟随机漫步
while True:
      rw=RandomWalk(50000)   #创建一个RandomWalk实例，将其包含的点都绘制出来
      rw.fill_walk()

      point_numbers=list(range(rw.num_points))
      plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=1)

      plt.scatter(0,0,c='red',edgecolor='none',s=10)  #起点
      plt.scatter(rw.x_values[-1],rw.y_values[-1],c='yellow',edgecolor='none',s=10) #终点

      plt.axes().get_xaxis().set_visible(False)
      plt.axes().get_yaxis().set_visible(False)
      plt.savefig('rw_visual.png',bbox_inches='tight')
      plt.show()

      keep_running=raw_input("Make another walk? (y/n):")   #input on python3
      if keep_running=='n':
      	break