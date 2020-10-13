## Warmup: Debugging

Fix the following code blocks by reading the Error output that the python
interpreter gives you.

```python
print('What could possibly be wrong here?'}
```

```python
a = 1
print('The ' + a + 'st Star Wars movie is the best one!')
```

```python
x = 4
y = 5
if x < y
    print(x, 'is less than', y, '!'

print('done!')
```

## Reading and writing files

Working with files in python requires understanding that there are three
distinct entities:

1. The file itself, as stored in the operating system's filesystem
2. The filename (or path), which is a string that points to the file
3. The python file object (technically a `TextIOWrapper` or `BufferedReader`),
   stored in some variable name. Once you create a python file object (by
   calling the `open` function on the filename), your code will only use the
   variable name that you assign to the file object.

### Reading

```python
joke_file = open('jokes.txt', 'r')  # 'r' = read mode
# read mode is default, so you can just write open('jokes.txt')
for line in joke_file:  # file objects are iterable (you can use a for loop on them)
    print(line)
joke_file.close()
```

The previous example works, but manually closing the file object is not the
best practice. Bad things can happen to your file if python stops while the
file is open. The best practice is to open a file using a `with` context block.
Python automatically closes the file when the block ends (or if it hits an
error in the middle of the block). The following idiom is highly preferred:

```python
with open('jokes.txt') as joke_file:  # name the file object joke_file
    for line in joke_file:
        print(line)
# joke_file.close() called automatically because the `with` code block ends
````

You can also read an entire file all at once. Note that in read mode, python
puts an imaginary cursor at the beginning of the file, and only moves forward.
Once you've read the file, if you try to read it again, it will return an empty
string (unless someone has added something to file after your first `read()`).

```python
with open('jokes.txt') as joke_file:
    jokes = joke_file.read()  # Get the entire file as one string
    print(len(jokes))  # How many characters are in the string?
    jokes_again = joke_file.read()  # The cursor is at the end now, so this returns an empty string
    print(len(jokes_again))
```

### Writing

Write mode deletes the file if it exists, then allows you to print to it. By
default, the `print` function prints to `stdout` (the terminal), but you can
tell it to print to your file by using the `file` keyword argument.

Run the following code and then use your preferred file manager to go find
`test_file.txt` in your file system.

```python
with open('test_file.txt', 'w') as test_file:  # 'w' = overwrite mode
    print('Hello file!', file=test_file)  # or test_file.write('Hello file!\n')
    # Notice that the end `\n` is automatic with `print`, but not file.write()
```

### Appending

```python
with open('test_file.txt', 'a') as my_file:  # 'a' = append mode
    print('Goodbye, file!', file=my_file)
```

`PRACTICE A`
Write a loop that writes 3 files: file0.txt, file1.txt, file2.txt. The
contents of file0.txt should be "This is file0.txt".


## Globs

Globs are a kind of simplified regular expression, usually used for selecting
files. Globs are especially common in bash terminal commands like ls, cp, mv,
etc.

https://en.wikipedia.org/wiki/Glob_(programming)#Syntax


`PRACTICE A`

Open a bash shell and navigate to the DIGHT360_Fall2017/activities/ folder.
Use the `ls` command to select files that...:
* ...end in `.py`
* ...begin with a capital letter
* ...have an s
* ...end in `.txt`
* ...begin with a 1
* ...has exactly eight characters


`PRACTICE B`

Now open a python shell in that same directory (type `python3` in bash).
```python
>>> from glob import glob
>>> glob('*.txt')
['jokes.txt']
```

Try the other patterns from PRACTICE A.


`PRACTICE C`

Write a python script that opens all the files in the current directory that
end with `.txt` and print each line that contains the letter 'r'.
