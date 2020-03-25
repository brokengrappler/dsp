[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> 


> def biased_pmf(pmf, label):
>    '''Input: unbiased PMF
>    Output: copy of pmf with bias PMF'''
>    new_pmf = pmf.Copy(label=label)
    
>    for x, p in pmf.Items():
>        new_pmf.Mult(x,x)

>    new_pmf.Normalize()
>   return new_pmf

> def graph_pmf(pmf1, pmf2):
>    thinkplot.Pmfs([pmf1, pmf2])
        

> resp = nsfg.ReadFemResp()
> under18 = resp.numkdhh

> under18_pmf = ts2.Pmf(under18)
> biased18_pmf = biased_pmf(under18_pmf, label='observed')

> print(under18_pmf.Mean())
> print(biased18_pmf.Mean())

> graph_pmf(under18_pmf,biased18_pmf)

