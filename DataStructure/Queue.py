# -*- coding: utf-8 -*-
'''
Created on 2017年11月30日
队列是一种先进先出的数据结构
@author: Jay
'''
from platform import node

class QueueNode:#队列节点类
    def __init__(self,value):
        self.value = value
        self.front = None
        self.rear = None
        
def getFront(queue):#取队头
    if isinstance(queue, QueueNode):
        if queue.front is not None:
            getFront(queue)
        else:
            return queue
    else:
        raise TypeError
    
def getRear(queue):#取队尾
    if isinstance(queue, QueueNode):
        if queue.rear is not None:
            getRear(queue)
        else:
            return queue
    else:
        raise TypeError
    
def inQueue(queue,value):#入队列
    if isinstance(queue, QueueNode):
        node = QueueNode(value)
        rear = getRear(queue)
        rear.rear = node
        node.front = rear
        return rear
    else:
        raise TypeError
    
def outQueue(queue):#出队列
    if isinstance(queue, QueueNode):
        front = getFront(queue)
        front = front.rear
        front.front = None
        return front
    else:
        raise TypeError

def printQueue(queue):
    while True:
        print queue.value
        if queue.rear is None:
            break
        else:
            queue = queue.rear
            