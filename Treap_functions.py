# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:08:00 2021

@author: divyam
"""

class Treapnode:
    def __init__(self,val,priority = None):
        self.val = val
        self.priority = priority
        self.left = None
        self.right = None

    
    

def insert(root,val,priority):
    if root is None:
        return Treapnode(val,priority)
 
    if val < root.val:
        if root.left:
            root.left = insert(root.left, val,priority)
        else:
            root.left = Treapnode(val,priority)
 
        # heapify ---> 
        if root.left and root.left.priority > root.priority:
            root = rotate_with_left_child(root)
    if val > root.val:
        if root.right:
            root.right = insert(root.right, val,priority)
        else:
            root.right = Treapnode(val,priority)
 
        # heapify
        if root.right and root.right.priority > root.priority:
            root = rotate_with_right_child(root)
 
    return root
        
def rotate_with_left_child(node):
    temp = node.left
    node.left = temp.right
    temp.right = node
    node = temp
    return node

def rotate_with_right_child(node):
    temp = node.right
    node.right = temp.left
    temp.left = node
    node = temp
    return node


def search(root, key):
    if (root is None):
        return False
    
    if  (key < root.val):
        return search(root.left, key)
        
    if  (key > root.val):
        return search(root.right, key)
        
    return True
