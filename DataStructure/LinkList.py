# -*- coding: utf-8 -*-
'''
Created on 2017年11月27日
链表是一种便于增加删除和增加新元素的数据结构
@author: Jay
'''

class Node(): #创建链表节点类
    def __init__(self,value,next=None):#初始化节点
        self.value = value 
        self.next = next
        
def CreatList(n):#生成链表
    if n<=0:
        return "Can't creat a empty LinkList"
    elif (n==1):#单一节点
        Node(1)
    else :#�多节点
        head = Node(1)#设置头节点
        tmp = head 
        for x in range(2,n+1):#循环添加节点进入链表
            tmp.next = Node(x)
            tmp = tmp.next#移动指针
        return head #返回头指针

def PrintList(head):#接收头指针，遍历链表
    p = head
    while p!=None:
        print p.value
        p = p.next
        
def GetLengthOfList(head):#取得链表的长度
    c = 0
    p = head
    while p!=None:
        c = c+1
        p = p.next
    return c 
    
def AppendNode(head):#在链表尾部添加新节点
    print "Please creat a new node"
    t = Node(value=raw_input("Give the node a value:"))
    p = head
    for x in range(1,GetLengthOfList(head)):#遍历链表到达表尾
        p = p.next
    p.next = t 
    return head

    
def InsertNode(head,n):#在链表内N处添加一个新节点
    if n<1 or n>GetLengthOfList(head):  
        return  
    
    print "Please creat a new node"
    t = Node(value=raw_input("Give the node a value:"))
    p = head
    for x in range(1,n-1):#遍历链表
        p = p.next
    t.next = p.next
    p.next = t
    return head

def DeleteNode(head,n):#删除N处的节点
    if n<1 or n>GetLengthOfList(head):  
        return  
    p = head
    t = head
    for x in range(1,n+1):
        p = p.next
    for x in range(1,n-1):
        t = t.next
    t.next = p
    return head 

    