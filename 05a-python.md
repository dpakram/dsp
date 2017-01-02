# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists are lists of values, numbered starting at 0. You can remove, add and change values in lists. Tuples are like lists, but their values cannot be changed. You can use tuples as keys in dictionaries because they are immutable- unable to be changed. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets cannot contain duplicates and they are unordered. Lists can have duplicates and are ordered starting at 0. To find an element in a set, you can use "contains". Indices cannot be used for sets because they are unordered. You can access an element in a list using its index. 

>> Example of set: Set(['John', 'Jane', 'Jack', 'Janice'])
>> Example of list: ['John', 'John', "Jack', 'Janice']

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is an anonymous or unbound function. It's a one statement function that returns something where the "return" is implied. You can use lambda with the sorted() function as the key object. For example, you can use it to sort through a list of "names":

>> sorted(list, key=lambda i: i.names)

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a tool for transforming one list, or any iterable, into another. Below are examples of a `for loop`, `list comprehension`, `map`, `filter`, `dictionary comprehension` and `set comprehension`.

>> for loop
>> ```python
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
return squared
```
>> list comprehension
```python 
items = [1, 2, 3, 4, 5]
squared = [i**2 for i in items]
```
>> map
```python
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```
>> filter
```python
items = [1, 2, 3, 4, 5]
def lessThanFour(element):
    return element < 4
            
filter(lessThanFour, items)
```
>> dictionary comprehension

format:
```python
{ key:value for item in list if conditional }
```
example:
```python
{ d['id']:d for d in data }.values()
```
>> set comprehension
```python
nums = set(n**2 for n in range(10))
```
>> The syntax for set comprehensions is almost identical to that of list comprehensions, but it uses curly brackets instead of square brackets.


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





