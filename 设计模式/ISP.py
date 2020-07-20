#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 23:34:57 2020

@author: chenjun
"""


from abc import abstractmethod,ABCMeta


class Animal(metaclass=ABCMeta):
    
    def __init__(self,name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    @abstractmethod
    def feature(self):
        pass
    
    @abstractmethod
    def moving(self):
        pass
    
class Irun(metaclass=ABCMeta):
    
    @abstractmethod
    def running(self):
        pass
    
class Ifly(metaclass=ABCMeta):
    
    @abstractmethod
    def flying(self):
        pass
    
class Inatatory(metaclass=ABCMeta):
    
    @abstractmethod
    def swimming(self):
        pass
    

class MammaAnimal(Animal,Irun):
    
    def __init__(self,name):
        super().__init__(name)
        
    def feature(self):
        print(self.name+'的生理特征：哺乳动物')
    
    def moving(self):   
        print('在陆地上跑')
        
    def running(self):
        print(self.name+'的生活方式',end='')
        self.running()
        
