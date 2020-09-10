
## Containers (`tuple`, `list`, `set`, `dict`, etc.)

Python containers are objects that store other objects.

### `tuple`

The simplest ordered container is the `tuple`. The tuple literal is expressed
using parentheses, and elements are separated using commas. Like strings, once
a tuple is created, it cannot be changed (In technical language, we say that
tuples are immutable.). You cannot add or take away elements. If you need a
tuple to change, you have to make a new tuple and replace the old one.

```python
>>> t1 = (3.14, 42, 'word', print)  # you can mix types in the same container
>>> t1
(3.14, 42, 'word', <built-in function print>)
>>> t1[3]  # indexing and slicing work just like strings
<built-in function print>
>>> t1[3]('hello world!')
hello world!
>>> t1[:2]
(3.14, 42)
>>> t2 = tuple('asdf')  # cast a str as a tuple
>>> t2
('a', 's', 'd', 'f')
>>> t3 = t1 + t2  # add tuples together
>>> t3
(3.14, 42, 'word', <built-in function print>, 'a', 's', 'd', 'f')
```

### `list`

If you need an ordered container like a tuple, but you want to be able to
append or remove elements, you need a `list`. List literals are expressed using
square brackets, with elements separated by commas. The most common method used
on lists is `append`.

```python
>>> list1 = list(t1)
>>> list1
[3.14, 42, 'word', <built-in function print>]
>>> list1[2]
'word'
>>> list1.append(t1)
>>> list1
[3.14, 42, 'word', <built-in function print>, (3.14, 42, 'word', <built-in function print>)]
>>> list1[4][2]
'word'
```

Strings have a builtin method to `split` the string into a list. By default, it
splits on whitespace (spaces, tabs, newlines, etc.), but you can tell it which
characters to split on, if you need to.

```python
>>> 'I want sausage, eggs, and spam.'.split()
['I', 'want', 'sausage,', 'eggs,', 'and', 'spam.']
>>> 'I want sausage, eggs, and spam.'.split('s')
['I want ', 'au', 'age, egg', ', and ', 'pam.']
>>> 'I want sausage, eggs, and spam.'.split('sa')
['I want ', 'u', 'ge, eggs, and spam.']
```

### `set`

Sets are ***unordered*** (hashed) containers that cannot hold duplicates. The
set literal is expressed using curly braces, with commas separating elements.
They are great for performing set theory operations (union, intersection,
difference, symmetric difference, etc.). In text processing, they are
frequently used to find *unique* tokens (words) in a list. Because they are
unordered, you cannot use indexing or slicing on sets.

```python
>>> sent = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'.split()
>>> sent
['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck', 'if', 'a', 'woodchuck', 'could', 'chuck', 'wood?']
>>> set1 = set(sent)
>>> set1
{'wood', 'How', 'much', 'wood?', 'could', 'if', 'would', 'woodchuck', 'a', 'chuck'}
>>> len(sent)
13
>>> len(set1)
10
>>> set1[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
>>> set2 = {1, 1, 1, 1, 1}
>>> set2
{1}
```

### `dict`

A dictionary is a container of key:value pairs. Instead of an index (based on
the order of the elements), a dictionary uses arbitrary keys to look up values.
The `dict` literal is expressed using curly braces and key:value pairs are
separated by commas. Just like a set, the keys of the dictionary are hashed,
so you cannot have duplicate keys.

```python
>>> dict1 = {'Rachael': 40, 'Rob': 39, 'Hyrum': 14, 'Eliza': 13, 'Wesley': 10, 'Mark': 8}
>>> dict1
{'Rachael': 40, 'Rob': 39, 'Hyrum': 14, 'Eliza': 13, 'Wesley': 10, 'Mark': 8}
>>> dict1['Rob']
39
>>> dict1['Methuselah'] = 969
>>> dict1
{'Rachael': 40, 'Rob': 39, 'Hyrum': 14, 'Eliza': 13, 'Wesley': 10, 'Mark': 8, 'Methuselah': 969}
```

##  Testing for membership using `in` a container

You can test whether an object is in a dict, list, set, str, tuple, etc.
using the keyword `in`:

```python
>>> 'i' in 'team'  # There is no I in team!
False
>>> 4 in [2, 3, 5, 7, 11, 13, 17, 19]
False
>>> 'Bob' in ['Alvin', 'Simon', 'Theodore']
False
>>> 'A' in ['Alvin', 'Simon', 'Theodore']  # must be equal to an element
False
```

## Loops

A loop is a block of code that is intended to repeat in some way. Loops are the
workhorse of programming.

### `while` loops

A `while` loop repeats until the given condition is `False`. It introduces a
block of code, so as you would expect, its line ends in a colon and the
following code block is indented.

```python
>>> x = 0
>>> while x <= 10:
...     print(x)
...     x += 1
...
0
1
2
3
4
5
6
7
8
9
10
```

This can be used to repeat an action for a user.

```python
>>> response = ''  # initialize the name response to avoid NameError in next line
>>> while response != 'stop':
...     response = input('What do you want to do? ')
What do you want to do? nothing
What do you want to do? soccer
What do you want to do? volleyball
What do you want to do? kayaking
What do you want to do? stop
>>>
```

### `for` loops (iteration)

A `for` loop goes through all the values in a sequence. You simply give it a
name to use on each iteration.

```python
>>> for name in ['Rob', 'Hyrum', 'Eliza']:
...     if name.startswith('R'):
...         print('Nice name, ' + name + '!')
...     else:
...         print('Okay name, I guess, ' + name + '.')
...
Nice name, Rob!
Okay name, I guess, Hyrum.
Okay name, I guess, Eliza.
```

You can use a for loop to filter a list.

```python
>>> output_list = []  # initialize the list to add things to
>>> for name in ['Rob', 'Hyrum', 'Eliza']:
...     if name.startswith('R'):
...         output_list.append(name)
...
>>> output_list
['Rob']
```

## `range` function

The `range` function is used to create a sequence of `int`s using the exact
same approach as the slice notation we already learned.

Imagine you want a range to some astronomically large number. To save memory,
python uses a simple generator to only calculate the next value you need. To
see all of the values that a `range` will output, you have to consume all the
values in a for loop, or a list function, or something like that. In the
following examples, I use the `list` constructor to show what the output of
`range` will be:

```python
>>> range(10)
range(0, 10)  # python is just saying this is, in fact, a range generator
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # making it into a list shows the output values
>>> list(range(3, 22, 7))
[3, 10, 17]
>>> list(range(0, 22, 7))
[0, 7, 14, 21]
>>> list(range(21, 5, -3))
[21, 18, 15, 12, 9, 6]
```

It is very common to loop over ranges.

```python
>>> for i in range(10):
...     if i % 2 == 0:
...         print(i, 'is an even number!')
...
0 is an even number!
2 is an even number!
4 is an even number!
6 is an even number!
8 is an even number!
```

## Python "standard library"

Python comes with lots of useful tools available in the "standard library".
https://docs.python.org/3/library/index.html

Some very commonly used modules include...
* re - regular expressions
* datetime - basic date and time types
* collections - useful variations on dicts, for example
* pprint - print objects prettily (with readable indentations)
* math
* random - random number generation and random sampling
* statistics
* os - interact with operating system (especially the filesystem)
* pickle - object serialization
* csv - read/write csv data files
* html - HTML


## Importing modules (`import`, `from`, and `as`)

The "namespace" is all of the names that have been assigned.
In other words, it is everything that is available to be used.

You can get a standard library module into the namespace by `import`ing it:

```python
import re
print('This is the contents of the `re` module:\n', dir(re))
```

You can also just import part of a module using `from`

```python
print('Let\'s try some math!')
from math import log
from math import e
print('What is the meaning of life, the universe, and everything?',
      log(e ** 42))  # 42
print('The value of e is', e)
```

As you import something, you can assign it a custom name using `as`

```python
print('Let\'s alias something as we import it!')
print('importing e...')
from math import e
print('importing e as wahoo...')
from math import e as wahoo
print('T/F: e and wahoo are equal:', e == wahoo)
```

To summarize, the following three approaches all achieve the exact same thing

```python
# approach 1
import statistics
avg = statistics.mean
print('The average of [1, 2, 3] is:', avg([1, 2, 3]))
# or...
# print('The average of [1, 2, 3] is:', statistics.mean([1, 2, 3]))

# approach 2
from statistics import mean
avg = mean
print('The average of [1, 2, 3] is:', avg([1, 2, 3]))
# or...
# print('The average of [1, 2, 3] is:', mean([1, 2, 3]))

# approach 3
from statistics import mean as avg
print('The average of [1, 2, 3] is:', avg([1, 2, 3]))
```
