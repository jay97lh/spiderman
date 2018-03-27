# -*- coding: utf-8 -*-
'''
Created on 2017年11月27日
栈是一种先进后出的数据结构
@author: Jay
'''

class StackNode:#栈节点类
    def __init__(self,value):#初始化栈节点
        self.value = value
        self.behind = None #前一个节点
        self.before = None #后一个节点
    

'''    
def isStack(func,stack):
    def func(stack):
    if isinstance(stack, StackNode):
        return func
    else:
        raise TypeError
'''    
   
def printStack(stack):#遍历栈+
    if isinstance(stack, StackNode):
        top = getTop(stack)#取栈顶
        while True:
            print top.value
            if top.before is None:
                break
            else:
                top = top.before
    else:
        raise TypeError

def getTop(stack):#取栈顶
    if isinstance(stack, StackNode):#判断是否是栈类型
        if stack.behind is not None:
            return getTop(stack.behind)#递归调用该方法知道到达栈顶
        else:
            return stack
    else:
        raise TypeError
                
def pushStack(stack,value):#入栈
    node = StackNode(value)
    if isinstance(stack, StackNode):#判断是否是栈类型
        top = getTop(stack)#取得栈顶
        node.before = top 
        node.before.behind = node
        getTop(stack)
    else:
        raise TypeError 
    
def popStack(stack):#出栈
    if isinstance(stack,StackNode):
        top = getTop(stack)
        top = top.before
        top.behind = None
        getTop(stack)
    else:
        raise TypeError 
    

