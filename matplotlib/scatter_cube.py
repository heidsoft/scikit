#!/usr/bin/python
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

x_values=list(range(1,5001))
y_values=[x**3 for x in x_values]

plt.scatter(x_values,y_values,c=x_values,cmap=plt.cm.Reds,edgecolor='none',s=40)
plt.axis([0,5500,0,55000000])

plt.show()