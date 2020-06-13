#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 21:18:38 2020

@author: chenjun

决策取样器

核心逻辑：
1.打出装备的一个多项概率分布
2.装备对属性的随机分配
3.装备对攻击的加成
4.条件伤害输出：比如拿到两个装备之后的伤害输出
"""

import numpy as np
from scipy.special import gamma, gammaln

#得球分布
class Multi():
    
    def __init__(self,p,rso=np.random):
        
        if not np.isclose(np.sum(p),1.0):
            raise ValueError('g概率不等于1')
            
        self.p = p
        self.rso = rso
        self.logp = np.log(p)
    
    def sample(self,n):
        #抽样
        return np.random.multinomial(n,self.p)

            
    def logpmf(self,x):
        #抽样情况
        n = np.sum(x)
        #第一项
        log_n_factorial = gammaln(n+1)
        #第二项：分母
        log_x_fac = gammaln(x+1)
        log_x_sumfac = np.sum(log_x_fac)
        #第三项L
        log_pi_xi = self.logp * x
        log_pi_xi[x==0] = 0 
        log_pi_sum  = np.sum(log_pi_xi)
        #计算累计概率
        log_pmf =  log_n_factorial - log_x_sumfac + log_pi_sum      
        return log_pmf
        

    def pmf(self,x):
        log_pmf = self.logpmf(x)
        return np.exp(log_pmf)
    

def main():
    p = [0,0.1,0.2,0.3,0.4]
    rso = np.random.RandomState(230489)
    rv = Multi(p,rso=rso)
    s1 = rv.sample(1)
    s2 = rv.sample(2)
    s5 = rv.sample(5)
    
    log1 = rv.logpmf(s1)   
    log2 = rv.logpmf(s2)   
    log3 = rv.logpmf(s5)
    
    p1 = rv.pmf(s1)
    p2 = rv.pmf(s2)
    p3 = rv.pmf(s5)

#写测试用例：
        
if __name__ ==  '__main__':
    main()
    
