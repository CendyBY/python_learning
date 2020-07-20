#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:43:46 2020

@author: chenjun

设计模式代码
"""


class Animal:
    '''
    动物类
    '''
    
    def __init__(self,name):
        self._name = name
        
    def running(self):
        print(self._name+'is running')
        
    def swimming(self): 
        print(self._name+' is swimming')
        
    
if __name__ == '__main__':
    
    Animal('猫').running()
    Animal('狗').running()
    
    Animal('fish').swimming()