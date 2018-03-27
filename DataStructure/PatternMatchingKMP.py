# -*- coding: utf-8 -*-
'''
Created on 2017��12��4��
KMP模式匹配相较于朴素模式匹配不用对i进行回溯，通过生成T字符串的NEXT[J]数组来进行模式匹配
@author: Jay
'''
def getNext(T,next):
    i,j = 1,0
    next[1] = 0
    while(i<T[0]):
        if (j==0 or T[i]==T[j]):
            i = i+1
            j = j+1
            next[i] = j
        else:
            j = next[j]  
            
def IndexKMP(S,T,pos):
    i,j = pos,0
    next = []
    getNext(T, next)
    while(i<=S[0] and j<=T[0]):
        if (j==0 or S[i]==T[i]):
            i = i+1
            j = j+1
        else:
            j = next[j]
    if (j>T[0]):
        return i-T[0]
    else:
        return 0
    
