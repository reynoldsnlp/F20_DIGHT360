## Warm-up

Try to understand why the following expressions give the output listed. Be
prepared to discuss.

#### Rise of the Nones

```python
>>> a = [print(i) for i in range(4)]
0
1
2
3
>>> print(a)
[None, None, None, None]
```

#### Leaking, sticky residue

```python
>>> for i in range(4):
...   pass
...
>>> print(i)
3
>>> b = [j for j in range(4)]
>>> print(j)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'j' is not defined
```

#### Unpack rat

```python
>>> x, y = [1, 2]
>>> x
1
>>> y
2
>>> (x, (y, z), p, (d, q, a), (s, a, p)) = [1, [2, 3], 4, [5, 6, 7], [8, 9, 10]]
>>> x
1
>>> y
2
>>> z
3
>>> a
9
>>> for name, age in [('Rob', 38), ('Rach', 39), ('Hyrum', 14)]:
...     print(f'{name} is {age} years old.')
...
Rob is 38 years old.
Rach is 39 years old.
Hyrum is 14 years old.
```

## Parsing HTML (for reals this time)

Regular expresssions are not ideal HTML parsers

In order to parse HTML, you need an HTML parser, like those included in
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start).
To install BeautifulSoup, run `python3 -m pip install --user bs4`.


```python
from bs4 import BeautifulSoup
import re

# open a previously saved HTML file and soupify it
# BeautifulSoup can take a str or a file object as its first argument
with open('Healthcare_in_Canada-wikipedia.html') as healthy_file:
    soup = BeautifulSoup(healthy_file, 'html.parser')
```

Let's find all the headers with \<h2\> tags in this article.

```python
print(soup.find_all('h2'))
```

Let's extract all of the links on this page.

```python
for a in soup.find_all('a'):
    print(a.get('href'))
```

Let's find all the \<span\> tags in this article with `id=Public_opinion`.

```python
print(soup.find_all('span', id='Public_opinion'))
```

Now find elements with 'poll' in the text.

```python
print(soup.find_all(string='poll'))
# or even better...
# print(soup.find_all(string=re.compile(r'\bpoll\b', re.I)))
```

## Homework warm-up

In the following dictionary, think of each key as a webpage, and its value as
pages that it links to. Write an algorithm that does the following:

1. Begin by putting `0` in a to-do list.
1. Make an empty set to keep track of pages you've already visited.
1. Write a loop that goes until the to-do list is empty.
    * `.pop()` an element out of your to-do list and get its links.
    * If the links have not yet been visited, add them to your to-do list.
    * Print the popped element and add it to the already-visited set.

```python
d = {0: [3, 1], 1: [0, 3], 2: [0, 1], 3: [0, 4], 4: [1, 3]}
todo = {0}
already_seen = set()  # calling `set` without arguments makes an empty set.
...
```

If done correctly, your algorithm should print every page except for `2`,
because no pages link to `2`.
