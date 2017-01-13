[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> ```Python
>> Use the NSFG respondent variable NUMKDHH to construct the actual distribution 
>> for the number of children under 18 in the household."""

>> #from __future__ import print_function


>> from chap01soln import ReadFemResp
>> import thinkstats2
>> import thinkplot

>> #call data
>> data = ReadFemResp()
>> data = data['numkdhh']

>> #create probability mass function (pmf)
>> pmf = thinkstats2.Pmf(data, 'Actual')

>> #create distribution as observed by sample responses
>> #The result is a new Pmf that represents
>> #the biased distribution

>> def BiasPmf(pmf, label):
>> 	new_pmf = pmf.Copy(label=label)

>> 	for x, p in pmf.Items():
>> 		new_pmf.Mult(x, x)

>> 	new_pmf.Normalize()
>>	return new_pmf

>> biased_pmf = BiasPmf(pmf, "Observed")
>> thinkplot.PrePlot(2)
>> thinkplot.Pmfs([pmf, biased_pmf])
>> thinkplot.Show(xlabel= 'Kids per Household', ylabel= 'Probability')
```
