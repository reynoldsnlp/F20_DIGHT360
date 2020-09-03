# 

## The python Read-Evaluate-Print Loop (REPL)

To enter the REPL, you type `python3` in a command line. (In VS Code, go to
`Terminal` | `New Terminal`.)  You should see the python prompt: `>>> `.

The REPL is an interactive command prompt where you can type a command and get
immediate feedback (as opposed to writing a script in a file, and then
executing the file all at once). In the REPL, the result of evaluated
expressions is always sent to `stdout` (displayed on the screen). (When you
execute a script, you have to use the `print` function to send things to
`stdout`.)

### Math

What do the following operators do? `+` `-` `*` `/` `**` `%`

Python has two main number types: `int` and `float`.

```python
>>> type(2)
<class 'int'>
>>> type(2.0)
<class 'float'>
>>> float(2)
2.0
>>> int(2.0)
2
>>> int(5.5)
5
>>> 2 + 2.0
4.0
```

### Variables

The `=` operator assigns a value to a variable name. Everything after `=` is
evaluated first, and the result is saved in the name you create before `=`. In
the case of `z = z * z` below, the `z * z` is evaluated first (`4 * 4` -> `16`)
and then that value replaces the previous value of `z`.

```python
>>> x = 2
>>> y = 2 + 0
>>> z = x + y
>>> z
4
>>> z = z * z
>>> z
16
```

### Strings (`str`)

In programming, text is called "strings", since they are strings of characters.
Python string literals are surrounded by quotation marks, `'hello'` or `"hello"`.
Strings can be "concatenated" using the `+` operator.

```python
>>> first = 'hello'
>>> second = 'world'
>>> first + ' ' + second + '!'
'hello world!'
```

## The `input` function

One way to get input from a user is the `input` function. You give the user
a prompt (a `str`), and the user can enter something.

```python
>>> quest = input('What is your quest? ')  # user types something, hits [enter]
>>> quest
'I seek the Holy Grail.'
```

Notice that `'I seek the Holy Grail'` is a string.

```python
>>> number = input('What number would you like to double? ')  # user types '2'
>>> number + number
'22'
```

What happened there? We have to cast the string `'2'` as an `int` or `float`.

```python
>>> number = input('What number would you like to double? ')  # user types '2'
>>> number = float(number)
>>> number + number
'4.0'
```

## Using `help()`

The built-in `help` function uses the same keys as the command-line tool `less`
to navigate:

* <kbd>q</kbd> quit / exit
* <kbd>f</kbd> forward / page down
* <kbd>b</kbd> backward / page up
* <kbd>&uarr;</kbd> up one line
* <kbd>&darr;</kbd> down one line

To search a document, type <kbd>/</kbd>, the text you are searching for,
<kbd>return</kbd>. Use <kbd>n</kbd> to find the `n`ext instance, and
<kbd>N</kbd> to find the previous instance.

1. Use the `help()` function to learn about the following built-in functions.
   Use them, tinker, break, learn.
   * `len()`
       * Try using `len()` on various types of values (`str`, `int`, `float`,
         `function`, etc.)
   * `abs()`
   * `chr()` / `ord()`
   * `pow()`
   * `round()`
   * `sorted()`

### Code formatting

The most widely accepted (and official) standard for python code formatting is
called [PEP-8](https://www.python.org/dev/peps/pep-0008/) ("PEP" means "Python
Enhancement Proposal"). The best way to learn how to write good-looking code is
to use a linter in your text editor. I recommend `flake8`.

You can also use a website to make sure our code is easier to read.  Put the
following code blocks into the input field at [this
website](http://pep8online.com/) to see how they can be improved.

```python
x=4
y=2
print(x,y,sep='')
```

```python
a = 42# this is a comment about life, the universe and everything
b = 'spam'
#the previous line is just great, mostly because it has the word 'spam' in it, which is so funny!

print( a )
```
