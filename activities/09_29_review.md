# Core Concepts Quiz Review

Some of these concepts are not technically review, but the point of today's
lesson is to slow down and round out the knowledge/skills that we have learned
so far.

## Using Python for...

* Concatenating strings and variables
* Regular expressions (cheatsheets allowed)
* Loops (`for` and `while`)
* Splitting strings
* Substituting text (`''.replace` or `re.sub`)
* Importing modules
* List comprehensions

## Builtin functions and objects

### Math functions

* `abs` (absolute value)
* `max`/`min`
* `round`
* `sum`

##### Less important math functions

* `bin` (binary representation of integer)
* `divmod` (division: returns (solution, remainder) tuple)
* `hex` (hexadecimal representation of integer)
* `oct` (octal representation of integer)
* `ord` (unicode codepoint of 1-character string)
* `pow` (same as `x ** y`, with some other bells and whistles)

### Logic functions

* `all`
* `any`

### Classes (types)

* `bool`
* `dict`
* `float`
* `int`
* `list`
* `set`
* `str`
* `tuple`

##### Less important classes

* `bytearray`
* `bytes` (like `str`, but pure bytes without assuming an encoding (unicode))
* `complex` (complex number, i.e. real and imaginary)
* `frozenset` (immutable set)
* `object` (class from which all other classes are inherited)

### Miscellaneous

* `chr`
* `dir`
* `enumerate`
* `exit`/`quit`
* `hash`
* `help`
* `id`
* `input`
* `isinstance`
* `len`
* `open`
* `print`
* `range`
* `reversed`
* `sorted`
* `type`
* `zip`

##### Less important miscellaneous

* `ascii`
* `callable`
* `classmethod`/`staticmethod`/`property` method decorators
* `compile`
* `delattr`/`getattr`/`hasattr`/`setattr`
* `eval`/`exec`
* `filter`
* `format`
* `globals`/`locals`
* `issubclass`
* `iter`
* `map`
* `memoryview`
* `next`
* `repr`
* `slice`
* `super`
* `vars`

## Reserved keywords 

The complete list of
[keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
can be found using the following code.  Examples of each keyword can be found
[here](https://www.programiz.com/python-programming/keyword-list).

```python
import keyword
print(keyword.kwlist)
```

* `def`/`return`
* `del`
* `and`/`or`/`not`
* `if`/`elif`/`else`
* (`from` X )`import` Y( `as` Z)
* `for`/`while`/`continue`/`break`
* `in`
* `is`
* `None`
* `pass`
* `True`/`False`
* `with`/`as`

##### Less important keywords (we'll learn a few of these later)

Do not worry about the following keywords that are generally more advanced.

* `assert`
* `async`/`await`
* `class`
* `lambda`
* `global`
* `nonlocal`
* `raise`
* `try`/`except`/`finally`
* `yield`

## Terms to know:

* IDE
* Function
* Module
* Debug
* Directory
* String
* Character
* Variable
* Value
* Regular expression


## Example questions

On the quiz, most of the questions simply ask you to describe as precisely as
possible what snippets of python code are doing. For example, given the
following snippet...

```python
import re

poem = 'I think that I shall never see a poem lovely as a tree.'
matches = re.findall(r'\bs\w+', poem)
print(matches)
```

...the following response would receive full credit:

> This snippet imports the `re` module, then declares a string under the name
> `poem`, then calls the `findall` function from the `re` module to find every
> word that begins with an `s` (shall and see). This list is assigned to the
> name `matches`. Finally, the list is printed to `stdout`.

