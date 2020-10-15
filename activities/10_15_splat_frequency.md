# Splat operator

(see https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists)

The `*` operator usually means multiplication, but it can also be used to
pack/unpack sequences. Recall how python can perform multiple assignment:

```python
>>> a, b = [1, 2]
>>> a
1
>>> b
2
```

Now see what happens when you have too many values to unpack:

```python
>>> a, b = [1, 2, 3, 4, 5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
```

The splat operator can fix it:

```python
>>> a, *b = [1, 2, 3, 4, 5]
>>> a
1
>>> b
[2, 3, 4, 5]
```

### Splat operator in functions

The most common place to see the splat operator is in function definitions:

```python
def a(x, y, *args, **kwargs):
    print('x:', x)
    print('y:', y)
    print('args:', args)
    print('kwargs:', kwargs)

a(1, 2, 3, 4, 5, spam=2, eggs=4)
```

...and with function calls:

```python
>>> print_dict = {'sep': '\t'}
>>> print(*'1234', **print_dict)
1	2	3	4
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```

### Splat with `zip()`

`PRACTICE: ` What happens with the `zip()` function when you use the splat
operator?

## Frequency distributions

The `Counter` class is a subclass of `dict` that automatically counts the
elements of any iterable (anything you can do a `for` loop over). After a
`Counter` has already been created, you can use the `update` method to keep
adding to the counts.

```python
from collections import Counter
counter = Counter('this is a sentence.')
print(counter)
# Counter({'s': 3, ' ': 3, 'e': 3, 't': 2, 'i': 2, 'n': 2, 'h': 1, 'a': 1, 'c': 1, '.': 1})
counter.update('this is another sentence. WOOOOOOOOOO!')
print(counter)
# Counter({'O': 10, ' ': 7, 'e': 7, 's': 6, 't': 5, 'n': 5, 'i': 4, 'h': 3, 'a': 2, 'c': 2, '.': 2, 'o': 1, 'r': 1, 'W': 1, '!': 1})
print(counter['O'])  # Lookup values by their key, just like a dict
# 10
print(counter['W'])
# 1
```


```python
from collections import Counter

# Counter of Batman theme song
song = 'na na na na na na na na na na na na na na na na Bat Man !'.split()
batman_counter = Counter(song)
print(batman_counter.most_common())
print(batman_counter.most_common(2))

# How frequent is "Bat"? (remember: Counter objects are sub-types of dict)
print(batman_counter['Bat'])
```

> PRACTICE

* Make a list of words that only occur once in `batman_counter`. ("singletons"
  or "hapaxes")
  * Remember that `dict` (and by inheritance, `Counter`) has a method `items`
    that gives a key-value pairs as a list of tuples: `[(key1, value1),
    (key2, value2), ...]`
  * A `for` loop would work, here. Can you also do it with a list
    comprehension?
