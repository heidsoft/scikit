#!/usr/bin/python
# -*- coding:utf-8 -*-
from sklearn.datasets import load_iris    #iris 鸢尾花卉数据集
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names) 
#读取iris的数据以表结构表示出来，iris以鸢尾花的特征作为行名(sepal length;sepal width;petal length;petal width)
#print df

df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75   #uniform() 方法将随机生成下一个实数，它在 [x, y) 范围内
#x=df['is_train']
#print x
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
#Categorical 分类数据
#显示种类  Categories (3, object): [setosa, versicolor, virginica]
#from_codes(codes,categories,ordered=False),ordered默认False;从代码和数组类别中创建分类类型
#y=df['species']
#print y
df.head()
#print df

train, test = df[df['is_train'] == True], df[df['is_train'] == False]
#is_train的数据为True时,将对应的Target传给train;is_train的数据为False时,将对应的Target传给test
#print train['species']
#print test['species']
features = df.columns[:4]     #Index([u'sepal length (cm)', u'sepal width (cm)', u'petal length (cm)',u'petal width (cm)'],
#print features
clf = RandomForestClassifier(n_jobs=2)
y, _ = pd.factorize(train['species'])  #将输入值编码为枚举类型或分类变量
clf.fit(train[features], y)
preds = iris.target_names[clf.predict(test[features])]
#print preds
print(pd.crosstab(test['species'], preds, rownames=['actual'], colnames=['preds']))  #交叉表

'''
交叉表
>>> df = pd.DataFrame({'key1':['a','a','b','b','a'],'key2':['one','two','one','two','one']})
>>> df
  key1 key2
0    a  one
1    a  two
2    b  one
3    b  two
4    a  one
>>> pd.crosstab(df.key1,df.key2) 
key2  one  two
key1          
a       2    1            个数
b       1    1
>>> pd.crosstab(df.key1,df.key2, margins=True) 
key2  one  two  All
key1               
a       2    1    3
b       1    1    2
All     3    2    5
'''