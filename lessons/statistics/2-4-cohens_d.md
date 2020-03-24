[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>import nsfg as ns
import math

def CohensD(group1, group2):
    # d = (x1-x2) / (pooled S)
    print('first born weight:', group1.mean(), '\n',
    'other\'s weight:', group2.mean())
    
    mean_diff = group1.mean() - group2.mean()
    n1 = len(group1)
    n2 = len(group2)
    pooled_var = (group1.var()*n1 + group2.var()*n2) / (n2+n1)
    CohensD = mean_diff / math.sqrt(pooled_var)
    return CohensD 

if __name__ == '__main__':
    preg = ns.ReadFemPreg()
    live = preg[preg.outcome==1]
    first = live[live.birthord ==1]
    others = live[live.birthord !=1]

    d = CohensD(first['totalwgt_lb'], others['totalwgt_lb'])
    print('Cohen\'s D:', d)
