# -*- coding: utf-8 -*-
'''
Created on 2017年12月5日
树是一种单对多的数据结构
@author: Jay
'''
#双亲表示法的树节点结构
class TreeNodeParent():
    def __init__(self,data):
        self.data = data
        self.parents = None
#添加长子域后双亲表示法的树节点结构
class TreeNodeParentFirstChild(TreeNodeParent):
    def __init__(self,data):
        super(TreeNodeParentFirstChild,self).__init__(data)
        self.parents = None
        self.firstchild = None
#添加右兄弟域后双亲表示法的树节点结构
class TreeNodeParentRightsib(TreeNodeParent):
        def __init__(self,data):
            super(TreeNodeParentRightsib,self).__init__(data)
            self.parents = None
            self.rightsib = None    
        
#孩子表示法的树节点结构
#使用孩子链表方法的孩子表示法树节点
class ChildListNode():#孩子链表节点
    def __init__(self,data):
        self.data = data
        self.next = None

class HeadListNode():#头指针链表节点
    def __init__(self,data):
        self.data = data
        self.firstchild = None

#双亲孩子表示法
#孩子链表结构同孩子表示法
class HeadListNodeParent(HeadListNode):#添加了双亲指针的头指针链表节点
    def __init__(self,data):
        super(HeadListNodeParent,self).__init__(data)
        self.firstchild = None
        self.parent = None
        



        



        

