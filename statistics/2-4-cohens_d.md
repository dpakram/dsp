[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

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
