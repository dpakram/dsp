[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> ``` python
>> import scipy.stats
```
>> set variables male population height (cm) mean and standard deviation
>> ``` python
>> mean = 178
>> stand_dev = 7.7
```

>> create normal distribution
>> ``` python
>> dist = scipy.stats.norm(loc = mean, scale = stand_dev)
```
>> computes mean and standard deviation from normal distribution
>> ``` python
>> print dist.mean(), dist.std()
```
>> mean = 178.0 and standard deviation = 7.7

>> find number of males between 5'10" and 6'1". set paramters and convert to cm
>> ``` python
>> low = dist.cdf(177.8)
>> high = dist.cdf(185.4)
>> print high-low
```
About 34% of males eligible for the blue man group, by height.
