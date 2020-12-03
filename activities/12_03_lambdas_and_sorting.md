## Lambda functions

Lambda functions are simple, disposable functions that have no name. In order
to demonstrate how they work, we will give them names by assigning them to
variables, but this is usually not how they are used. The next section will
show an excellent use case for lambdas.

Let's say we want a function to return the second element of a sequence.
Here is the standard way to declare a function:

```python
def std_func(x):
    """Return second element of sequence."""
    return x[1]
```

...and here is how to achieve the same thing using lambda notation:

```python
lamb_func = lambda x: x[1]  # we don't usually assign a lambda to anything
```

Although saving the `lambda` function is a strange thing to do, it results in a
function that is virtually identical to a normal function:
 
```python
std_func([0, 1])
# 1
lamb_func([0, 1])
# 1
```

> PRACTICE A

Write lambda functions to do the following:
  * always return 4
  * given a string, return the string in lower-case
  * return the last element of a sequence
  * print whatever it is given
  * Add up all the elements in a sequence (cast strings as floats)

## Sorting with keys and/or reversed

The `sorted` function returns a list of elements in sorted order. Setting the
`reverse` keyword argument to `True` sorts in reverse order.

```python
names = [('Rachael', 40), ('Rob', 39), ('Hyrum', 15), ('Eliza', 13), ('Wesley', 11), ('Mark', 8)]
sorted(names)
# [('Eliza', 13), ('Hyrum', 15), ('Mark', 8), ('Rachael', 40), ('Rob', 39), ('Wesley', 11)]
sorted(names, reverse=True)
# [('Wesley', 11), ('Rob', 39), ('Rachael', 40), ('Mark', 8), ('Hyrum', 15), ('Eliza', 13)]
```

print('Sorting "keys" are not the same kind of key as in dict key-value pairs.')

`sorted` sorts by using `>` and `<` operators. By default it compares the
entire elements. Tuples (and really all sequences) are compared by their first
item first, and subsequent items if needed.

What if we want to sort by a specific part of the tuple?

```python
# Sorting by the second item of the tuple (age)
sorted(names, key=std_func)
# [('Mark', 8), ('Wesley', 11), ('Eliza', 13), ('Hyrum', 15), ('Rob', 39), ('Rachael', 40)]
sorted(names, key=lambda x: x[1])  
# [('Mark', 8), ('Wesley', 11), ('Eliza', 13), ('Hyrum', 15), ('Rob', 39), ('Rachael', 40)]
```

The two calls to `sorted` above are equivalent, since they pass a function as
the keyword argument `key` that selects the second item. Notice that we are not
calling these functions because they do not have `()`. We are passing the
function itself as an argument. Also note that with the lambda expression, you
do not have to declare the function elsewhere in your code. Lambda functions
are "single-use" or "disposable" functions.

> PRACTICE B:

Sort `names` by...
    * the second letter of the name
    * the last letter of the name
