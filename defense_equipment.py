#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
运算王者荣耀装备机制
"""
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

################  2.装备带来增益计算
'''
一级：初始生命值HP=3041，物理防御护甲AR=91，物理穿透ARP=55，魔抗PR=50
可承受最大物理伤害
四级：初始生命值HP=3586，物理防御护甲AR=145，物理穿透ARP=55，魔抗PR=75
八级：初始生命HP=4312，物理防御护甲AR=217，物理穿透ARP=55，魔抗PR=109
十二级：初始生命HP=5039，物理防御护甲AR=290，物理穿透ARP=55，魔抗PR=143
十五级满级时：初始生命HP=5584，物理防御AR=344，物理穿透ARP=55，魔抗PR=169
'''
HP=np.array([3041,3586,4312,5039,5584])
AR=np.array([91,  145, 217, 290, 344])
ARP=np.array([55, 55,  55,  55,  55])

max_AD=HP*(602+AR-ARP)/602

max_AD_sub=[]

for idx in range(0,len(max_AD)-1):
    max_AD_sub.append(round(max_AD[idx+1]-max_AD[idx]))

print("1，4，8，12，15级可承受最高AD伤害")
print(max_AD.astype(np.int))
print("可承受最大伤害差值：")
print(max_AD_sub)

#布甲+90，守护铠+210，反伤甲+420
print("220，承伤增益布甲AR+90:")
enhanced_AD=HP*(602+AR+90-ARP)/602-max_AD
print(enhanced_AD.astype(np.int)) #增益量
print((enhanced_AD/220*100).astype(np.int)) #100金币增益量
print("730，承伤增益守护铠+210")
enhanced_AD=HP*(602+AR+210-ARP)/602-max_AD
print(enhanced_AD.astype(np.int))
print((enhanced_AD/730*100).astype(np.int)) #100金币增益量
print("1840,承伤增益反伤甲+420")
enhanced_AD=HP*(602+AR+420-ARP)/602-max_AD
print(enhanced_AD.astype(np.int))
print((enhanced_AD/1840*100).astype(np.int)) #100金币增益量


#红水晶
print("300,红水晶HP+300：")
enhanced_AD=(HP+300)*(602+AR-ARP)/602-max_AD
print(enhanced_AD.astype(np.int))
print((enhanced_AD/300*100).astype(np.int)) #100金币增益量

#力量腰带
print("900,力量腰带HP+1000:")
enhanced_AD=(HP+1000)*(602+AR-ARP)/602-max_AD
print(enhanced_AD.astype(np.int))
print((enhanced_AD/900*100).astype(np.int)) #100金币增益量

#霸者重装
print("2070,霸者重装HP+2000:")
enhanced_AD=(HP+2000)*(602+AR-ARP)/602-max_AD
print(enhanced_AD.astype(np.int))
print((enhanced_AD/2070*100).astype(np.int)) #100金币增益量

#不祥征兆
print("2180,不祥征兆：HP+2000，AR+270:")
enhanced_AD=(HP+1200)*(602+AR+270-ARP)/602-max_AD
print(enhanced_AD.astype(np.int))
print((enhanced_AD/2180*100).astype(np.int)) #100金币增益量

#红莲斗篷
print("1830,红莲斗篷：HP+1000，AR+240:")
enhanced_AD=(HP+1000)*(602+AR+240-ARP)/602-max_AD
print(enhanced_AD.astype(np.int))
print((enhanced_AD/1830*100).astype(np.int)) #100金币增益量

print("1830+2180，红莲加不祥征兆")
enhanced_AD=(HP+1000+1200)*(602+AR+240+270-ARP)/602-max_AD
print(enhanced_AD.astype(np.int))
print((enhanced_AD/(1830+2180)*100).astype(np.int)) #100金币增益量

print("Program done!")
