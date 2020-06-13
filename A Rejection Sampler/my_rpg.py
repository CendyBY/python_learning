#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 00:27:00 2020

@author: chenjun



"""

import pandas as pd
import numpy as np
import my_multi as mm
import matplotlib.pyplot as plt
import seaborn as sns

class MultiStat():
    
    def __init__(self,bonus_prob,stats_prob,rso=np.random):
        
        
        self.stats_name = ("dexterity", "constitution", "strength",
                   "intelligence", "wisdom", "charisma")
        self.bonus = mm.Multi(bonus_prob,rso=rso)
        self.stats = mm.Multi(stats_prob,rso=rso)
        
    def sample(self):
        
        bonus = self.bonus.sample(1)
        bonus = np.argmax(bonus)
        
        stats = self.stats.sample(bonus)
        
        return dict(zip(self.stats_name,stats))
    
    def logpmf(self,items):
        
        stats = np.array([items[i] for i in self.stats_name])
        
        n =np.sum(stats)
        
        bonus_logpmf = self._bonus_logpmf(n)
        
        stats_logpmf = self.stats.logpmf(stats)
        
        logpmf = bonus_logpmf + stats_logpmf
        
        return logpmf
        
    def _bonus_logpmf(self,n):
        
        
        if n<0 or n>len(self.bonus.p):
            return -np.inf
            
        _sample = np.zeros(len(self.bonus.p))
        _sample[n] = 1 
        return self.bonus.logpmf(_sample)
    
        
        
    
    def pmf(self, items):
        
        logpmf = self.logpmf(items)
        
        pmf = np.exp(logpmf)
        
        return pmf
        
    
class DamageDis():
    
    def __init__(self,bonus_num,stats_dist,damage_num=12,hits=1,rso=np.random):

        self.bonus_num = bonus_num
        
        self.damage = np.array(range(1,damage_num+1))
        self.damage_dist = mm.Multi(np.ones(damage_num)/float(damage_num),rso = rso)
        
        self.stats_dist = stats_dist
        
        self.hits = hits
        
        self.rso = rso
        
        
    def sample(self):
        
        items = [self.stats_dist.sample() for i in range(self.bonus_num)]
        
        #属性加成      
        strength = np.sum([stat['dexterity'] for stat in items])
        
        #属性对攻击力的加成
        hit_nums = self.damage_dist.sample((1+strength) * self.hits)
        
        
        #属性对攻击力的加成
        damage = np.sum(hit_nums * np.array(self.damage))
        
        return damage
        
    
    
if __name__ == '__main__':
    bonus_probs = np.array([0.0, 0.55, 0.25, 0.12, 0.06, 0.02])
    stats_probs = np.ones(6) / 6.0
    rso = np.random.RandomState(234892)
    #装备属性分布
    item_dist = MultiStat(bonus_probs,stats_probs,rso)
    
    print(item_dist.sample())
    print(item_dist.sample())
    print(item_dist.sample())
    
    item = item_dist.sample()
    print(item)
    
    print(item_dist.logpmf(item))
    
    print(item_dist.pmf(item))
    
    
    damage_dist = DamageDis(2, item_dist, hits=3, rso=rso)
    
    samples = np.array([damage_dist.sample() for i in range(100000)])
    
    print(samples.min())
    
    print(samples.max())
    
    print(np.percentile(samples, 50))


    sns.distplot(samples,bins=60)
    plt.show()
    