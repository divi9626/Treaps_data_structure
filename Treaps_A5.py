# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:54:51 2021

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

letters = ['Z','Y','X','W','V','Q','U','P','S','R','K','J','G','B','F','C','M','D','H','I','L','A','N','O','T','E']
priorities = [24,7,14,17,26,10,8,18,22,4,5,16,13,19,23,12,2,20,21,25,15,6,11,3,9,1]

keys = []

for letter in letters:
    keys.append(letter)

root = None
for i in range(len(keys)):
    root = insert(root,keys[i],priorities[i])
    
f = open("textbook.txt", encoding="utf8")
file_text = f.read()
file_text = file_text.replace("\n", " ")

all_tokens = file_text.split(' ')
all_characters = [ch for token in all_tokens for ch in token ]

LOW_CASE_RANGE = (97, 122)
UPPER_CASE_RANGE = (64, 90)
alphabets = set.union(set(range(*LOW_CASE_RANGE)), set(range(*UPPER_CASE_RANGE)))

def is_alphabet(ch):
    return ord(ch) in alphabets

def start_processing():
    for ch in all_characters:
        #ch = ch.upper()
        if is_alphabet(ch):
            # search in the treap
            if search(root,ch.upper()):
                print(True)
            else:
                print(False)
import time
start = time.clock()
start_processing()
end = time.clock()
print(end - start)