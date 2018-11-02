# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:11:57 2018

@author: gs716
"""
class problem2:
    def __init__(self):
        self.alist =[]
        
    def add(self,a):
        self.alist.insert(0,a)
    def remove(self):
        print(self.alist.pop())
    def getValue(self,i):
        if i < len(self.alist):
            print(self.alist[i])
        else:
            print(-1)
