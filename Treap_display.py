# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:28:32 2021

@author: divyam
"""

import random

class Treapnode:
    def __init__(self,val):
        self.val = val
        self.priority = random.randrange(0,100)
        self.left = None
        self.right = None
        
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    
    

def insert(root,val):
    if root is None:
        return Treapnode(val)
 
    if val < root.val:
        if root.left:
            root.left = insert(root.left, val)
        else:
            root.left = Treapnode(val)
 
        # heapify ---> 
        if root.left and root.left.priority > root.priority:
            root = rotate_with_left_child(root)
    if val > root.val:
        if root.right:
            root.right = insert(root.right, val)
        else:
            root.right = Treapnode(val)
 
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

letters = ['Z','Y','X','W','V','Q','U','P','S','R','K','J','G','B','F','C','M','D','H','I','L','A','N','O','T','E']

keys = []
for letter in letters:
    keys.append(letter)
    
root = None
for i in range(len(keys)):
    root = insert(root,keys[i])
    
b = root
b.display()


