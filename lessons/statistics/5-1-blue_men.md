[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```python
#5'10" and 6'1" unit conversion based on 1 in. = 2.54 cm
bm_min = 70*2.54
bm_max = 73*2.54
print(bm_min, bm_max)
bm_minCDF = dist.cdf(bm_min)
bm_maxCDF = dist.cdf(bm_max)
print(bm_minCDF,'\n',bm_maxCDF,'\n', bm_maxCDF-bm_minCDF)
```
