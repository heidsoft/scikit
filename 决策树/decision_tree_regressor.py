#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
from sklearn import tree

x=[[0,0],[10,10]]
y=[0.5,2.5]
clf=tree.DecisionTreeRegressor()
clf=clf.fit(x,y)
print(clf.predict([[1,1]]))   #回归和分类不同的是向量y可以是浮点数，x必须是整数
'''
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

rng=np.random.RandomState(1)
x=np.sort(5*rng.rand(80,1),axis=0)
y=np.sin(x).ravel() #ravel()将数组拉直(多维数组降为一维数组),与y=np.sin(x)对比即知区别
y[::5]+=3*(0.5-rng.rand(16))   #切片.所有数,每5个取1个数
#a=len(x)
#print a
#print x
#print y

regr_1=DecisionTreeRegressor(max_depth=2)
regr_2=DecisionTreeRegressor(max_depth=5)
#决策树的最大深度，默认可以不输入，如果不输入的话，决策树在建立子树的时候不会限制子树的深度。
#一般来说，数据少或者特征少的时候可以不管这个值。如果模型样本量多，特征也多的情况下，推荐限制这个最大深度，具体的取值取决于数据的分布。常用的可以取值10-100之间。
regr_1.fit(x,y)
regr_2.fit(x,y)

x_test=np.arange(0.0,5.0,0.01)[:,np.newaxis]  #与x_test=np.arange(0.0,5.0,0.01)对比即知区别,第一个参数为显示数据的起始点
#print x_test
y_1=regr_1.predict(x_test)
y_2=regr_2.predict(x_test)
#print y_1
#print y_2

plt.figure()
plt.scatter(x,y,c="darkorange",label="data")  #点的颜色标注
plt.plot(x_test,y_1,color="cornflowerblue",label="max_depth=2",linewidth=2) #线条的颜色标注
plt.plot(x_test,y_2,color="yellowgreen",label="max_depth=5",linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()  #显示右上角图例
plt.savefig('decision_tree_regressor.png',bbox_inches='tight')
plt.show()