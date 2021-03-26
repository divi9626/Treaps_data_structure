# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:36:48 2021

@author: divyam
"""
import random

class Treapnode:
    def __init__(self,val):
        self.val = val
        self.priority = random.randrange(0,100)
        self.left = None
        self.right = None

    
    

def insert(root,val):
    if root is None:
        return Treapnode(val)
 
    if val < root.val:
        if root.left:
            root.left = insert(root.left, val)
        else:
            root.left = Treapnode(val)
 
        # heapify ---> 
#        if root.left and root.left.priority > root.priority:
#            root = rotate_with_left_child(root)
    if val > root.val:
        if root.right:
            root.right = insert(root.right, val)
        else:
            root.right = Treapnode(val)
 
        # heapify
#        if root.right and root.right.priority > root.priority:
#            root = rotate_with_right_child(root)
 
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