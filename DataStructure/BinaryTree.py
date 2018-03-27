# -*- coding: utf-8 -*-
'''
Created on 2017年12月5日
二叉树是一种度最高为2且左右节点分次序排列的有限的树的结构
@author: Jay
'''
class BinaryTreeNode():#二叉树结点
    def  __init__(self,data):
        self.data = data 
        self.lchild = None
        self.rchild  = None

class BinaryTree():#二叉树类
    def __init__(self):
        self.root = None
    def add(self,data):
        if self.root is None:#当根节点为空时初始化根节点
            self.root = BinaryTreeNode(data)
        else:
            bitree = [self.root]#生成包含二叉树的列表
            while True :
                node = bitree.pop(0)
                if node.lchild == None:
                    node.lchild = BinaryTreeNode(data)
                    return 
                elif node.rchild == None:
                    node.rchild = BinaryTreeNode(data)
                    return
                else:
                    bitree.append(node.lchild)
                    bitree.append(node.rchild)                    
    #使用递归方式遍历二叉树
    def PerOrderTraverse(self,root):#前序遍历二叉树
        if root is None:
            return []
        result = [root.data]
        left_child = self.PerOrderTraverse(root.lchild)
        right_child = self.PerOrderTraverse(root.rchild)
        return result + left_child + right_child
    
    def InOrderTraverse(self,root):#中序遍历二叉树
        if root is None:
            return []
        left_child = self.InOrderTraverse(root.lchild)
        result = [root.data]
        right_child = self.InOrderTraverse(root.rchild)
        return left_child + result + right_child
    
    def PostOrderTraverse(self,root):#后续遍历二叉树
        if root is None:
            return []
        left_child = self.PostOrderTraverse(root.lchild)
        right_child = self.PostOrderTraverse(root.rchild)
        result = [root.data]
        return left_child + right_child + result

