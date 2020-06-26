[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

```python
import math

m = 1000
n = 10
lam = 2

# mean = 1/L, therefore L = 1/mean
# median = ln(2) / m
# xs = np.random.exponential

means = []
medians = []

for _ in range(m):
    xs = np.random.exponential(1/lam, n)
    L = 1 / np.mean(xs)
    Lm = math.log(2) / np.median(xs)
    means.append(L)
    medians.append(Lm)

import seaborn as sns
import matplotlib.pyplot as plt

sns.distplot(means)
```
![Distribution](https://github.com/brokengrappler/dsp/blob/master/lessons/statistics/8.2PDF.png)
```python
#standard error and CI of 90%
MSE = [(estimate-lam)**2 for estimate in means]
RSM = math.sqrt(np.mean(MSE))
print(RSM)

x = np.sort(means)
y = np.arange(1, len(x)+1) / len(x)
plt.plot(x,y)
plt.xlabel('Means')
plt.ylabel('CDF')

#z-score of 90% is 1.645. you can use norm.ppf to get the z-score.
lowCI = lam - RSM*1.645
upCI = lam + RSM*1.645
print(lowCI,upCI)
```
![CDF](https://github.com/brokengrappler/dsp/blob/master/lessons/statistics/8.2CDF.png)
