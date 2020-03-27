[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

```python
#Standardized Moment is kth central moment divided by (sample std)^k
from math import sqrt

def StandardizedMoment(xs,k):
    var = CentralMoment(xs,2)
    std = sqrt(var)
    return CentralMoment(xs,k) / std**k

# Standardized Moment 3
def Skewness(xs):
    return StandardizedMoment(xs,3)

#Pearson's median skewness coefficient

def PearsonsSkew(xs):
    PSmedian = Median(xs)
    PSmean = RawMoment(xs,1)
    PSvar = CentralMoment(xs,2)
    PSstd = sqrt(PSvar)
    return 3*(PSmean-PSmedian)/PSstd

if __name__ == '__main__':
    print('Skewness:', Skewness(sample))
    print('Pearson\'s:', PearsonsSkew(sample))
```
