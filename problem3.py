# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:34:34 2018

@author: gs716
"""

from problem2 import *
class ProblemThree():
  
    def __init__(self):
        self.alist =[]
        
    def add(self,a):
        self.alist.insert(0,a)
    def remove(self):
        return self.alist.pop()
    def getValue(self,i):
        if i < len(self.alist):
            print(self.alist[i])
        else:
            print(-1)
    def search(self,value):
        i = 1
        found = False
        while found == False:
            if(self.remove() == value):
                print("Number of comparisons: " + str(i))                
                found = True
            else:
                i = i + 1
