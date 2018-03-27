# -*- coding: utf-8 -*-
'''
Created on 2017年12月1日
朴素的模式匹配算法是通过一趟趟遍历需要匹配的子串与主串来完成的
进行模式匹配的串将 串长记录在串的开头
@author: Jay
'''

def index(S,T,pos):#S作为主串，T作为子串
    if S[0] < 0 or T[0] < 0 :
        raise TypeError
    elif pos < 1 or pos > S[0]:#pos标记匹配起点
        raise ValueError
    else:
        i,j = pos,1
        while i<=S[0] and j<=T[0]:
            if S[i]==T[j]:#当出现匹配的字符时开始一个个向后匹配
                i = i + 1
                j = j + 1
            else:#当出现不匹配字符时pos回到原匹配起点的后一个位置
                i = i - j + 2
                j = 1
        if j > T[0]:#j>T[0]表示子串T完全被匹配
            return i-T[0] #返回匹配位置起点
        else:
            return 0 


