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

You can get a standard library module into the namespace by `import`ing it.

```python
>>> import re
>>> print('This is the contents of the `re` module:\n', dir(re))
['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'RegexFlag', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_alphanum_bytes', '_alphanum_str', '_cache', '_compile', '_compile_repl', '_expand', '_locale', '_pattern_type', '_pickle', '_subx', 'compile', 'copyreg', 'enum', 'error', 'escape', 'findall', 'finditer', 'fullmatch', 'functools', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'template']
```

The `import` statement always begins by looking in the current directory, so if
you name your python files the same as modules in the standard library (e.g.,
`re.py`), then it will import your module instead of the standard library
module, and you will be confused.

You can also import just a part of a module using `from`:

```python
>>> from math import e
>>> from math import log
>>> print('What is the meaning of life, the universe, and everything?', log(e ** 42))
What is the meaning of life, the universe, and everything? 42
>>> print('The value of e is', e)
The value of e is 2.718281828459045
```

As you import something, you can assign it a custom name using `as`

```python
>>> from math import e
>>> from math import e as wahoo
>>> print(e == wahoo)
True
```

To summarize, the following three approaches all achieve the exact same thing

```python
# APPROACH 1
import statistics
avg = statistics.mean
print('The average of [1, 2, 3] is:', avg([1, 2, 3]))
# or...
# print('The average of [1, 2, 3] is:', statistics.mean([1, 2, 3]))

# APPROACH 2
from statistics import mean
avg = mean
print('The average of [1, 2, 3] is:', avg([1, 2, 3]))
# or...
# print('The average of [1, 2, 3] is:', mean([1, 2, 3]))

# APPROACH 3
from statistics import mean as avg
print('The average of [1, 2, 3] is:', avg([1, 2, 3]))
```

## List comprehensions

List comprehensions are a very succint, efficient and "readable" (eventually!) syntax
for transforming or filtering a sequence. The following two examples achieve the
same thing:

```python
>>> cities = ['Salt Lake City', 'Provo', 'Orem', 'Paris', 'Moscow', 'New York']
>>> output_list = []
>>> for city in cities:
...     if city.startswith('P'):
            output_list.append(city)
...
>>> output_list
['Provo', 'Paris']
>>>
>>>
>>> output_list = [city for city in cities if city.startswith('P')]
>>> output_list
['Provo', 'Paris']
```

To understand a list comprehension, start by reading at `for`; everything
before the `for` expresses the value that you want in the resulting list.

> PRACTICE
> Write list comprehensions that return...
> 1. ...the name of every city that has the letter 'e' in it
> 2. ...the first letter of every city that has the letter 'e' in it
> 3. ...the name of every city backwards
> 4. ...the last letter of every city that has the letter 'a' in it
> 5. ...1 for every city in the list. (i.e. [1, 1, 1, 1, 1, 1])
> 6. ...42 for every city that ends with a vowel. Assume y is a vowel. (i.e. [42, 42])


## Regular expressions

If you are new to regular expressions, the tutorial at https://regexone.com/ is
highly recommended!

Regular expressions are a powerful syntax to match patterns in text. Every
major programming language has a regular expression engine, and unfortunately
there are slight differences between languages. We will use regex101.com to
test our regexes, but make sure to click on `Python`, or else it will use the
wrong engine! Also run each regex on your own machine to see how to actually
implement it in a script, e.g. `import re`, `re.search(pattern, text, flags)`.

```python
>>> import re
>>> re.search('word2', 'word1 WORD2 word3', flags=re.IGNORECASE)
<_sre.SRE_Match object; span=(6, 11), match='WORD2'>
>>> re.findall('word2', 'word1 WORD2 word3', flags=re.IGNORECASE)
['WORD2']
```

#### Backslash hell

tl;dr: when you write regular expressions, use "raw strings", meaning put an
`r` right before the string literal: `r''` instead of `''`. Note that the input
box on regex101.com has `r"` at the beginning to indicate that it will
interpret your regular expression as if it were written in a raw string
literal.

Recall that python string literals have an escape character (the backslash `\`)
that allows you to do things like put a single quote inside of single quotes.
For example, `'\''` is equivalent to `"'"`. This raises a problem: how to you
put a backslash in a python string literal? The answer is to escape the
backslash with another backslash (`'\\b'` represents `\b`). As long as the
backslash is not the last character of the string, you can also use "raw
strings" (`r'\b'`).

Regular expressions have many symbols that combine a backslash with another
character (`\w`, `\b`, `\s`, etc.) and backslash is also the escape character
for regular expressions (so to match a backslash, you need two backslashes), so
you should generally always use raw strings to limit how many backslashes you
have to write.

| --- | --- | --- |
| actual | string literal | raw string literal |
| --- | --- | --- |
| `\` | `'\\'` | N/A (ends with backslash) |
| `\b` | `'\\b'` | `r'\b'` |
| `\\` | `'\\\\'` | `r'\\'` |

## Regular expression practice

1)  a string with "ed" at the end
2)  a word with "ed" at the end
3)  a word with "anti" at the beginning
4)  both the American and British spellings of "labour/labor"
5)  'Jack', 'Mack', 'Pack'
6)  both the American and British spellings of "center/centre"
7)  an eight-letter word with 'j' as the third letter and 't' as the sixth letter
8)  words other than "best" that end in "est"
9)  a more concise regex than "(make|makes|made)"
10) two words next to each other with the same final letter
    * `Hint`: Use parentheses to capture and then "\1" to match the previously caught match.)
11) modify the previous regex to not consume the second word (so that it's available for another search)
    * `Hint`: Use positive lookahead, that is, "(?=...)"
12) The bracketed portion of "Thi{s is a first example s}entence."
    * `Hint`: Use greedy matching.
13) The bracketed portions of "Thi{s is} a fir{st example s}entence."
    * `Hint`: Use lazy/non-greedy matching.
14) Words that begin with "t" regardless of case, that is, "T" and "t", in the following sentence: "The deal is that I make dinner every night, but Juanito made it last night."
    * `Hint1`: Look up the "re.IGNORECASE" parameter of the re.findall() function.
    * `Hint2`: "re.IGNORECASE" has an abbreviation of "re.I".
    * `Hint3`: You may need to escape the word boundary character "\b" with an additional backslash, that is, "\\b".
