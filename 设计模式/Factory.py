#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 23:20:10 2020.

@author: chenjun

工厂模式
"""

# 模拟故事剧情

from abc import abstractclassmethod, ABCMeta

class Coffee(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    def getName(self):
        """函数说明."""
        return self.name

    @abstractclassmethod
    def getTaste(self):
        pass


class LatteCoffee(Coffee):

    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return '轻柔而香醇'


class MochaCoffee(Coffee):

    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return '丝滑与醇厚'


class Coffeemaker:

    @staticmethod
    def makeCoffee(coffeeBean):
        if coffeeBean == '拿铁咖啡dou':
            coffee = LatteCoffee('拿铁')
        elif coffeeBean == 'moke':
            coffee = MochaCoffee('moke')
        else:
            raise ValueError('ddd')
        return coffee


if __name__ == '__main__':

    def testCoffeeMaker():
        latte = Coffeemaker.makeCoffee('拿铁咖啡dou')
        print()
