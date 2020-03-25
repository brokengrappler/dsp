[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> 


> def biased_pmf(pmf, label):<br>
> <t>    '''Input: unbiased PMF
> <t>   Output: copy of pmf with bias PMF''' <br>
> <t>   new_pmf = pmf.Copy(label=label) <br>
    
>    for x, p in pmf.Items(): <br>
>        new_pmf.Mult(x,x) <br>

>    new_pmf.Normalize() <br>
>   return new_pmf <br>

> def graph_pmf(pmf1, pmf2): <br>
>    thinkplot.Pmfs([pmf1, pmf2]) <br>
        
<p>
resp = nsfg.ReadFemResp()
under18 = resp.numkdhh

under18_pmf = ts2.Pmf(under18)
biased18_pmf = biased_pmf(under18_pmf, label='observed')

print(under18_pmf.Mean())
print(biased18_pmf.Mean())

graph_pmf(under18_pmf,biased18_pmf)
</p>
