### Functions

We have already learned to use several built-in python functions, like `print`,
`help`, etc. Functions are just chunks of code that you can reuse by calling
them. In python, we call a function by putting parentheses (`()`) right after
the function name, like `print()`, `help()`, or `exit()`.

You can define your own functions using the `def` and `return` keywords. Note
the colon at the end of the line that triggers an indented code block. All of
the code indented after the colon are part of the function.

```python
def add_two_numbers(x, y):
    print('Adding', x, 'and', y, '...')
    total = x + y
    return total
    print('This line will never be executed because it comes after `return`.')
```

If we call this function by typing `return_value = add_two_numbers(2, 5)`, it
will print `'Adding 2 and 5 ...'`, then it will assign the sum 2 and 5 to the
*local* variable `total` (in the function's own private namespace).  Then it
will return the value of `total`, which is `7`. This value will then be stored
in `return_value`.

Every function ***must*** return a value, but you don't have to include the
`return` statement. If you do not have a `return` statement, your function will
return `None`. 

#### Practice

Write a function called `F2C` that converts Faregnheit to Celsius (you can copy
some of your code from the homework you just turned in).


### Comparisons and Booleans (True/False)

In order to compare values, python has several comparison operators.

* `>`  greater than
* `>=` greater than or equal
* `<`  less than
* `<=` less than or equal
* `==` equal (note the difference between `=` assignment and `==` comparison)
* `!=` not equal

Try to predict how python will evaluate the following expressions. Check to see
if you are right.

```python
4 == 4
4 == 4.0
5.1 == 5.1000000
'sparrow' == 'sparrow'
'Sparrow' == 'sparrow'
'a' < 'z'
'Sparrow' < 'sparrow'
's' > 10
2 < 3 < 4 < 100 < 1000
4 == 4.0 == 16 ** 0.5
```

The output of a comparison is either `True` or `False`. These are called
"boolean" values. In python, `True` is actually just a special version of the
integer `1`, and `False` is a special version of `0`. So `4 == 4 + 'a' < 'z'`
evaluates to `True + True` which then evaluates to `2`.

Comparisons can be combined using `and` and `or`. Can you figure out which one
comes first in the order of operations? You can use parentheses to override the
order of operations.

### Control flow (`if`, `elif`, and `then`)

You can make code execution conditional by using the `if`, `elif`, and `then`
keywords. Just like function definitions, these keywords have a colon at the
end of the line and the following indented lines belong to them.

```python
def verify_age(age):
    if age > 120:
        print('You are dead.')
        return False
    elif >= 18:
        print('Legally, you are an adult!')
        return True
    else:
        print('Legally, you are not an adult.')
        return False
```

The code in an `elif` block is only executed if the preceding `if` condition is
`False`, so in the above code `elif age >= 18:` is implicitly the same as if it
said `elif 120 > age >= 18:` because the `if` condition above it already
captures values above 120.

### Indexing and slicing

Several python objects are "sequences" (including strings!), meaning that they
can contain multiple elements that are arranged in a set order. Python has a
very convenient way to reference elements in a sequence, using square brackets
(`[` and `]`). The first element in the sequence has the index `0`, the second
element `1`, and so on. The following example shows how to reference an index.

```python
>>> s = 'spam'
>>> s[0]
's'
>>> s[3]
'm'
>>> s[-1]
'm'
>>> s[3] + s[2] + s[1] + s[0]
'maps'
```

A "slice" of a sequence is like an index, but it can reference multiple
elements.  A slice consists of three numbers: the start index, the end index,
and the stepwise value.  By default, the start index is the beginning, the end
index is the end, and the stepwise value is `1`, so a default slice is just a
copy of the original sequence.

```python
>>> 'This is a longer string'[5:15:3]
'iaoe'
>>> s
'spam'
>>> s[1:]  # start=1, end=default, step=default
'pam'
>>> s[2:]  # start=2, end=default, step=default
'am'
>>> s[:1]  # start=default, end=1, step=default
's'
>>> s[:2]  # start=default, end=2, step=default
'sp'
>>> s[::2]  # start=default, end=default, step=2
'sa'
>>> s[::-1]  # negative stepwise makes it start at the end and work backwards
'maps'
>>> s[::-2]
'mp'
```

### A deeper dive into strings (`str`s)

> A "method" is a function that is attached to an object.

Object attributes are accessed using the `.` character, so `my_obj.pi` is a
reference to `pi` which is stored "inside" `my_obj`. In the following example,
`title` is a method of the string `'moby dick'`.

```python
>>> 'moby dick'.title
<built-in method title of str object at 0x10c695330>
>>> 'moby dick'.title()
'Moby Dick'
```

Use `help(str)` function to discover all of the (many!) methods that are
attached to `str`s. Ignore the double-underscore ("dunder" or "magic")
methods, which are for behind-the-scenes interactions. You can call them,
just like any other method, but they are not generally intended for that.


Start with the following methods and then explore on your own. Use, tinker,
break, learn.

* `startswith()` / `endswith()`
* `isdigit()` / `isnumeric()` / `isdecimal()`
* `islower()` / `isupper()` / `istitle()`
* `lower()` / `upper()` / `title()` / `swapcase()`
* `zfill()`
