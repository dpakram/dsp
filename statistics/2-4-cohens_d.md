[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> Cohen's d= d = (x_1 − x_2) / s
>> where x_1 and x_2 are the means of the groups and s is the “pooled standard deviation”. 
>> In my code I used the thinkstats2 module to call the CohenEffectSize(group1, group2) function, which computes cohen's d. For a break down of the code that makes up this function go to 2.9 "Effect Size": http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24
>> The results returned show a value of -0.0886729270726 when comparing "first" babies to "other" babies. 

>> ``` python
>> from __future__ import print_function

>> import sys
>> from operator import itemgetter

>> import first
>> import thinkstats2
>> import math



>> def WeightDifference(live, firsts, others): 
>>     return thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

>> def main(script):
>>     """Tests the functions in this module.

>>     script: string script name
>>     """
>>     live, firsts, others = first.MakeFrames()
>>     hist = thinkstats2.Hist(live.prglngth)

>>     # explore the weight difference between first babies and others
>>     print(WeightDifference(live, firsts, others))


>> if __name__ == '__main__':
>>     main(*sys.argv)
    ```
