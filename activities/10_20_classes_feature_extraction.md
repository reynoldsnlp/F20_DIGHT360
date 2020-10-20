## Python `class`es

We are already familiar with several types of objects in Python: `str`, `list`,
`float`, `int`, `dict`, `set`, `tuple`, etc. You can also make your own custom
objects using the `class` keyword. Think of a class like a cookie cutter. It
is the tool that defines what the cookie will look like, but it isn't a cookie.
Each thing that the class generates is an "instance" of the class.

```python
class A:
    def woot(self):  # define a "method" (a function that belongs to a class)
        # the first argument of every method is usually `self`, which refers
        # to the instance of the class. In this case, I don't actually use
        # `self`, but it has to be there anyway.
        print('Hooray!')

a = A()
type(a)
# <class '__main__.A'>
a.woot()  # This is shorthand for `A.woot(a)`
# Hooray!
```

The example class `A` above is a minimal class. Classes can also inherit from
existing classes to take advantage of all the methods and attributes of the
parent class:

```python
class MyList(list):
    def woot(self):
        print('Hooray!')

my_list = MyList(range(10))
my_list
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list.woot()
# Hooray!
```

## Feature extraction

We are working toward building a machine-learning classifier that will be able
to classify documents according to genre/register. The algorithms don't
actually look at the texts, they only care about numbers. Therefore, the input
to our machine-learning algorithms is a list of "features" that we extract from
any given document. You should think about what things you can count that might
differ between genres.

As an example, let's consider counting what proportion of the words are 1st
person pronouns. We would write something like the following function to
compute this value.

```python
def pro1_tr(tokens):
    """Compute 1st person pronoun-token ratio for input Text.

    tokens -- list of strings
    """
    pro1_count = len([token for token in tokens
                      if re.match(r'(?:i|me|my|mine)$', token, re.I)])
    return pro1_count / len(tokens)
```

After writing several functions, the following code can be used to extract
several features from every text in the corpus and write the features to a
tab-separated file.

```python
with open('05_output.tsv', 'w') as out_file:
    print('filename', 'ttr', '1st-pro', '2nd-pro', '3rd-pro', 'punct',
          'subcorpus', sep='\t', file=out_file)
    for filename in glob('Mini-CORE/*.txt'):
        with open(filename) as the_file:
            raw_text = clean(the_file)
	doc = nlp(raw_text)
	tokens = [token.text for token in doc]
        print(filename, ttr(tokens), pro1_tr(tokens), pro2_tr(tokens),
              pro3_tr(tokens), punct_tr(tokens), subcorp(filename),
              sep='\t', file=out_file)
```


### Normalization

Raw counts of some features are difficult/impossible to compare directly between
texts. For example, imagine that one document with 10,000 words has
200 instances of the word "me" and another document with only 2,000 words also
has 200 instances of the word "me". Obviously the second document has a much
higher rate of "me"s, but if you use the raw count, there does not appear to
be a difference. We need to *norm* the values, by dividing by the total number
of something (in this case, words), to be able to compare the documents. In the
first document, 0.02 of the words are "me", and in the second document, 0.1 of
the words are "me". Norming helps to show that the second document has a higher
rate.
