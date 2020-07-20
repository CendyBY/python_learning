#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 23:07:16 2020

@author: chenjun

依赖倒置原则

"""

from abc import abstractmethod,ABCMeta

class Animal(metaclass=ABCMeta):
    
    def __init__(self,name):
        self.name = name
        
    def eat(self,food):
        if self.check_food(food):
            print(self.name + '进食' + food.getName())
        else:
            print(self.name + '不吃' + food.getName())
            
    @abstractmethod
    def check_food(self,food):
        '''检查哪种食物可以吃'''
        pass
    
class Dog(Animal):
    
    def __init__(self):
        super().__init__('狗')
        
    def check_food(self,food):
        return food.category() == '肉'
    
class Swallow(Animal):
    
    def __init__(self):
        super().__init__('燕子')
        
    def check_food(self,food):
        return food.category() == '昆虫'
    
class Food(metaclass=ABCMeta):
    
    def __init__(self,name):
        self.name = name
        
    def getName(self):
        return self.name
    
    @abstractmethod
    def category(self):
        pass
    
    @abstractmethod
    def nutrient(self):
        pass
    
    
class Meat(Food):
    
    def __init__(self):
        super().__init__('肉')
        
    def category(self):
        return '肉'
    
    def nutrient(self):
        return '蛋白质，脂肪'
    
class Worm(Food):
    
    def __init__(self):
        super().__init__('昆虫')
        
    def category(self):
        return '昆虫'
    
    def nutrient(self):
        return '蛋白质含有微量元素'
    
if __name__ == '__main__':
    
    dog = Dog()
    swallow = Swallow()
    meat = Meat()
    worm = Worm()
    
    dog.eat(meat)
    
    dog.eat(worm)
    
    swallow.eat(worm)
    
    swallow.eat(meat)
