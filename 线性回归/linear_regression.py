#!/usr/bin/python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression  #一个估计器,scikit中所有的估计器都带有fit(),predict()

def runplt():
      plt.figure()            #设置绘图窗口的尺寸，figure函数用于指定图表的高度，宽度，分辨率，背景色
      plt.title("Height-Weight")
      plt.xlabel("Height")
      plt.ylabel("Weight")
      plt.axis([150,190,40,90])
      plt.grid(True)    #设置网格颜色和线性
      return plt

plt=runplt()
x=[[155],[157],[166],[177],[187]]
y=[[55],[60],[63],[70],[79]]
plt.plot(x,y,'k.')     #类似scatter()，散点图
#plt.savefig('linear_regression.png',bbox_inches='tight')  #第一个实参指定以什么样的文件保存图表，第二个实参指定将图表多余的部分裁剪掉

#plt.show() 

#创建并拟合图形
model=LinearRegression()
model.fit(x,y)  #分析模型参数(拟合)
print('预测身高180厘米同学的体重:$%.2f' %model.predict(np.array([170]).reshape(-1,1))[0])  #predict()是通过fit()算出的模型参数构成的模型，对解释变量进行预测获得的值

#残差预测值
y2=model.predict(x)
plt.plot(x,y,'k.')
plt.plot(x,y2,'g-')
for idx,x in enumerate(x):    #列举,枚举;enumerate()获取元素的值
     plt.plot([x,x],[y[idx],y2[idx]],'r-')

plt.show()

print('残差平方和: %.2f' % np.mean((model.predict(x) - y) ** 2))   #公式见图片
#测试集
x_test=[[156],[163],[166],[170],[188]]
y_test=[[56],[63],[63],[72],[80]]
print('R方:',model.score(x_test,y_test))      #r-squared也叫确定系数，表示模型对现实数据拟合的程度,公式见图片