#!/usr/bin/python
# -*- coding:utf-8 -*-

import pygal
from die import Die

die_1=Die()                #创建一个D6
die_2=Die(10)

results=[]               #掷几次骰子，并将结果存储在一个列表中
for roll_num in range(1000):
     result=die_1.roll()+die_2.roll()
     results.append(result)

frequencies=[]

max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
     frequency=results.count(value)
     frequencies.append(frequency)

#print(results)
#print(frequencies)
hist=pygal.Bar()     #对结果进行可视化

hist.title="Results of rolling a D6 and a D10 1000 times"
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title="Results"
hist.y_title="Frequency of Resuslt"

hist.add('D6+D10',frequencies)
hist.render_to_file('different_dice.svg')     #渲染为一个svg文件