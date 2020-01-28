#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
运算王者荣耀装备机制
"""
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
 
################  1.实际伤害比例与护甲值计算
plt.figure(1)
 
# 比例显示与运算
AR=[]
AD_ratio=[]
 
AR_all=np.linspace(0,1500,10) # 0-1500之间的护甲值
 
for AR_item in AR_all:
    AR.append(AR_item)
    AD_ratio.append(602/(602+AR_item)*100)
 
# 画图显示
plt.plot(AR,AD_ratio,marker='o')
plt.xlim(0,1500)
plt.grid( color = 'blue',linestyle='-',linewidth = 0.3)
plt.ylim(0,100)
 
for a, b in zip(AR, AD_ratio):
    a=round(a,0) #规定一位精度
    b=round(b,1)
    plt.text(a, b, (a,b),ha='center', va='bottom', fontsize=10)
 
plt.title('护甲与AD伤害比例%', fontproperties="SimSun")
plt.xlabel('AR护甲', fontproperties="SimSun")
plt.ylabel('AD受到伤害比例', fontproperties="SimSun")
#plt.show()
 
# 表格显示
 
AR=[]
AD_ratio=[]
ratio_decrese=[]
AR_all=np.linspace(0,1500,16) # 0-1500之间的护甲值,第三个参数是值的数量
for AR_item in AR_all:
    AR.append(round(AR_item,0))
    AD_ratio.append(round(602/(602+AR_item)*100,2))
    ratio_decrese.append(round((602/(602+AR_item)-602/(602+AR_item+100))*100,2))
df = pd.DataFrame(index=AR)
df["AD_ratio"]=AD_ratio
df["ratio_decrese"]=ratio_decrese
 
HEADER = '''
    <html>
        <head>
            <meta charset="UTF-8">
        </head>
        <body>
    '''
FOOTER = '''
        <img src="%s" alt="" width="1200" height="600">
        </body>
    </html>
    '''
with open("C:\\Users\\xingxiangrui\Desktop\\照片\\test.html", 'w') as f:
    f.write(HEADER)
    f.write(df.to_html(classes='df'))
    f.write(FOOTER)
 
print("Program done!")
