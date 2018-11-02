# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:05:30 2018

@author: gs716
"""
class ExamSort():
    def __init__(self,a,size):
        self.alist = a
        self.size = size
        
    def split(self):
        middle = (self.size - 1)//2
        leftSide = self.alist[0,middle]
        rightSide = self.alist[middle + 1,len(self.alist)]
        split2(leftSide,0,middle)
        split2(rightSide,middle + 1,len(self.alist))
        
    def split2(self,alist,first,last):
        middle = (self.size - 1)//2
        leftSide = self.alist[0,middle]
        rightSide = self.alist[middle + 1,len(self.alist)]
        while len(alist) > 1:
            split2(leftSide,0,middle)
            split2(rightSide,middle + 1,len(self.alist))
        
      
        