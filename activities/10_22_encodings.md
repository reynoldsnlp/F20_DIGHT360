# `ord` and `chr`

To get the UTF-8 decimal value of a character, use `ord`:

```python
ex = 'eggs and spam'
print(ex)
ords = [ord(char) for char in ex]
print('ords:', ords)
print('To look up a character based on its UTF-8 decimal value, use `chr`:')
chrs = [chr(num) for num in ords]
print('chrs:', chrs)
```

`PRACTICE A`

Use `ord` and `chr` to find where different alphabets are stored in unicode.
How many alphabet ranges can you identify?


# `bytes`

UTF-8 is not the only encoding. In fact, it is only one of the newest encodings
to be invented.
[Video by Tom Scott on Computerphile](https://www.youtube.com/watch?v=MijmeoH9LT4)

Python 2 was terrible at encodings; the `str` object could have been bytes in
any encoding. Python 3 solved this by making all str objects unicode (utf8).
Python 3 also introduced a `bytes` object that can store a string of bytes in
an arbitrary encoding, just like python2's `str`.

There are 2 ways to declare a bytes object:

```python
u = 'This is a test.'
b1 = bytes(u, encoding='utf8')
b2 = b'This is a test.'  # defaults to ascii
print('u:', type(u), u)
print('b1:', type(b1), b1)
print('b2:', type(b2), b2)

print('Are `str`s the same as `bytes`?', u == b1)
print('Are `b1` and `b2` the same?', b1 == b2)
```

The bytes literal `b''` syntax defaults to ascii encoding, so why are b1 (utf8)
and b2 (ascii) equivalent?

UTF-8 is a superset of ASCII (All the letters in the ASCII codec have
the exact same values in UTF-8). `bytes` objects do not know how they came to
be (i.e. which encoding was used to produce them). They are just bytes, so
there is no difference between ASCII-encoded ASCII and UTF8-encoded ASCII.

# decimal vs hex

```python
print('dec\thex')
for i in range(36):
    print(i, hex(i), sep='\t')
```

Python interpreter understands hex: just prefix w/ `0x`. The interpreter
evaluates a hex literal as an int.

```python
print(10, 0xa)
```

Non-ascii bytes in a `bytes` object are displayed as hex values: `\x__`

```python
cyrillic_bytes = bytes('Россия', encoding='utf8')
print('Россия in bytes:', cyrillic_bytes, len(cyrillic_bytes))
# Notice that the cyrillic characters use 2 bytes each.

# You can look at the decimal values of each byte by iterating:
print('cbl:', [i for i in cyrillic_bytes])
```

`PRACTICE B`

What is the hex literal for 42?  101?  212?
(Try to figure these out without using `hex`)



# Standard encodings

Before the Unicode Consortium brought order to the encoding galaxy, each
language had its own ecosystem of encodings that were developed.  Python has
codecs for virtually every encoding that you will encounter built in to the
`codecs` module:

https://docs.python.org/3/library/codecs.html#standard-encodings

These encodings can be used to open files (in text mode), or encode/decode
`bytes` objects.


## Reading/writing files in different encodings

`open()` defaults to encoding utf8, but you can give it other encodings.

```python
with open('encodings/cp1251_example.txt', encoding='cp1251') as cp1251_file:
    cp1251 = cp1251_file.read()
print(cp1251, type(cp1251))  # This is now a UTF-8 str
```

Writing to files is similar. Python3 automatically converts from the
UTF-8 str object to the encoding of the file.

```python
with open('encodings/koi8_r_example.txt', 'w', encoding='koi8_r') as k_file:
    k_file.write(cp1251)
```


## Reading/writing in binary

So far, we have always used `open` in text modes (r/w/a). However, `open` can
also open files in binary modes (rb/wb/ab). Note that there is no encoding
argument when you open in binary mode! Why not?

```python
with open('encodings/cp1251_example.txt', 'rb') as cp1251_file:
    cp1251 = cp1251_file.read()
print(cp1251, type(cp1251))  # This is a bytes object in 1251 encoding
utf8_rus = cp1251.decode('cp1251')  # This is now a UTF-8 str

# To write in binary, we need a `bytes` object of the desired encoding.
koi8r = utf8_rus.encode('koi8_r')  # same as bytes(cp1251, encoding='koi8_r')
with open('koi8_r_binary.txt', 'wb') as k_file:
    k_file.write(koi8r)
```


## 'Windows.... *sigh*

Windows has been unforgivably slow to adopt unicode. If you work in
Windows, you may sometimes get unexpected codec errors, because python
automatically detects the environment encoding, which will NOT be unicode. In
this case, just declare the `utf8` encoding explicitly:

```python
with open('that_one_file.txt', 'r', encoding='utf8') as f:
    ...
```
