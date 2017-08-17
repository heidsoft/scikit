#!/usr/bin/python
# -*- coding:utf-8 -*-

from numpy import genfromtxt  #创建数组表格数据
from sklearn.ensemble import RandomForestClassifier

dataset=genfromtxt('data.csv',delimiter=',')
#print dataset  #将文件的数据以数组的格式打印出来
x=dataset[1:,0:4]
y=dataset[1:,4]
clf=RandomForestClassifier(n_jobs=2,oob_score=True)
#n_jobs;用几个核并行，设置成2表示两个核并行训练
#oob_score :即是否采用袋外样本来评估模型的好坏.默认识False.推荐设置为True，因为袋外分数反应了一个模型拟合后的泛化能力。
clf=clf.fit(x,y)

print(clf.predict_proba([[33,0,80,1],
                               [100,0,10,1]]))
#predict_proba返回的是一个n行k列的数组，第i行第j列上的数值是模型预测第i个预测样本的标签为j的概率,每一行的和应该为1
#[[ 0.7  0.3]  不能得到相亲机会的概率(0)为0.7,能得到相亲机会的概率(1)为0.3
# [ 1.   0. ]]  不能得到相亲机会的概率(0)为1,能得到相亲机会的概率(1)为0
