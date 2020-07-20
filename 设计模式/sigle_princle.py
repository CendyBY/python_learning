#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:53:12 2020

@author: chenjun

前两个原则的练手
"""


class TerrestrialAnimal():
    
    def __init__(self,name):
        self._name = name
        
    def running(self):
        print(self._name+' is runnng')
        
    
class AquaticAnimal():
    
    def __init__(self,name):
        self._name = name
        
    def swimming(self):
        print(self._name+' is swimming')      
        
'''
新添加动物园功能

class Zoo():
    
    def __init__(self):
        self._animal = [
            TerrestrialAnimal('Dog'),
            AquaticAnimal('Fish')]
        
    def displayActivity(self):
        for animal in self._animal:
            if isinstance(animal,TerrestrialAnimal):
                animal.running()
            else:
                animal.swimming()
                
如果新添加一个鸟类不符合封闭开放原则
'''
from abc import ABCMeta,abstractmethod

class Animal(metaclass=ABCMeta):
    '''动物'''
    def __init__(self,name):
        self._name = name
        
    @abstractmethod
    def moving(self):
        pass
    
class TerrestrialAnimal(Animal):
    
    def __init__(self,name):
        super().__init__(name)
        
    def moving(self):
        print(self._name+' is running')
        
class AquaticAnimal(Animal):
    
    def __init__(self,name):
        super().__init__(name)
        
    def moving(self):
        print(self._name+' is swimming')
        
class BirdAnimal(Animal):
    
    def __init__(self,name):
        super().__init__(name)
    
    def moving(self):
        print(self._name+' is flying')


class Mokey(TerrestrialAnimal):
    
    def __init__(self,name):
        super().__init__(name)
        
    def climbing(self):
        print(self._name+'climing Tree')
        
        
class Zoo():
    
    def __init__(self):
        self._animals = []
        
    def addAnimal(self,animal):
        self._animals.append(animal)
        
    def displayActivity(self):
        for animal in self._animals:
            animal.moving()
            
    def mokeyClimbing(self,mokey):
        mokey.climbing()
        
        

if __name__ == '__main__':
    
    
    zoo = Zoo()
    zoo.addAnimal(TerrestrialAnimal('dog'))
    zoo.addAnimal(AquaticAnimal('fish'))
    zoo.addAnimal(BirdAnimal('bird'))
    mokey = Mokey('mokey')
    zoo.addAnimal(mokey)
    zoo.displayActivity()
    
    zoo.mokeyClimbing(mokey)