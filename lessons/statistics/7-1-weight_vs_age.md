[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

```pythong
percents = [75, 50, 25]

bins = np.arange(15, 45, 5)
indices = np.digitize(live.agepreg, bins)
groups = live.groupby(indices)

babywgt_cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]
age_mean = [group.agepreg.mean() for i, group, in groups]

for percent in percents:
    weights = [cdf.Percentile(percent) for cdf in babywgt_cdfs]
    label = '%dth' % percent
    thinkplot.Plot(age_mean, weights, label=label)

thinkplot.Config(xlabel='age (years)',
                ylablel='weight(lbs)')
```
