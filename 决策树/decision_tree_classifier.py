#!/usr/bin/python
# -*- coding:utf-8 -*-

from numpy import genfromtxt  #创建数组表格数据
from sklearn import tree
#加载数据
dataset=genfromtxt('data.csv',delimiter=',')   #delimiter:分割字符串，默认是任何空格
x=dataset[1:, 0:3]   #0到2列数据
y=dataset[1:, 3]     #第3列数据
#print x
#print y
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
#预测
print(clf.predict([[0,0,50]]))  #house:0;married:0;income:50
#输出[0.]代表不满足贷款要求