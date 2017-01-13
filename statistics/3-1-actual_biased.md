[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)
>>
```python

>> from chap01soln import ReadFemResp
>> import thinkstats2
>> import thinkplot
```
>> Call the data
```python
>> data = ReadFemResp()
>> data = data['numkdhh']

>> #create probability mass function (pmf)
>> pmf = thinkstats2.Pmf(data, 'Actual')
```
>> Create a distribution as observed by sample responses.
>> The result is a new Pmf that represents the biased distribution
```python
>> def BiasPmf(pmf, label):
>> 	new_pmf = pmf.Copy(label=label)

>> 	for x, p in pmf.Items():
>> 		new_pmf.Mult(x, x)

>> 	new_pmf.Normalize()
>>	return new_pmf

>> biased_pmf = BiasPmf(pmf, "Observed")
```
>> Plot the actual versus the oberseved (biased) number of children per household
```python
>> thinkplot.PrePlot(2)
>> thinkplot.Pmfs([pmf, biased_pmf])
>> thinkplot.Show(xlabel= 'Kids per Household', ylabel= 'Probability')
```
>> Find the pmf and biased means
```python
>> print 'Actual mean', pmf.Mean()
>> print "Observed mean", biased_pmf.Mean()
```
>> Actual mean 1.02420515504
>> Observed mean 2.40367910066
