# Web scraping

## Warmup: nesting functions and operations

How much work should you do in each line of code? A good rule of thumb is that
each line of code should be equivalent to a simple English sentence. If you
have to say more than one sentence to describe what a line of code is doing,
you should consider whether it would be better to split it into more lines. This
usually involves creating single-use, intermediate variables. If you use good
descriptive variable names, this helps to self-document what the code is doing.

One drawback is that single-use, intermediate variables may make your reader
wonder whether this value is going to be used somewhere else. You have to
consider what is best for your code.

`PRACTICE`

Refactor the following code blocks as one line:

```python
x = 2 + 2
x_str = str(x)
sent = 'My favorite number is ' + x_str
print(sent)
```

```python
# assume that `import re` was already executed
match = re.search(r'(\b[A-Z][a-z]+\b)\s+\b([A-Z])', 'Robert Reynolds')
groups = match.groups()
first_name = groups[0]
print(first_name)
```

Refactor the following line of code into multiple lines:

```python
print(all_lines_from('my_file.txt'))
```

### Ethics of web scraping

https://medium.com/towards-data-science/ethics-in-web-scraping-b96b18136f01

###  Brief introduction to HTML

HTML is a markup language that defines document content/structure:
learn as much as you want here:

https://www.w3schools.com/html/html\_intro.asp
https://www.w3schools.com/html/html\_basic.asp

For our purposes, you just need to know that there are lots of different
elements in HTML with start tags and end tags. The end tag is exactly like
the start tag, but with a slash: `<p>This is a paragraph.</p>`

HTML elements can nest, but to be well-formed a nested element must close
before its parent: `<h1>This heading has a <p>paragraph in it.</p></h1>`
NOT well-formed:   `<h1>This heading has a <p>paragraph in it.</h1></p>`

Technically, regular expressions cannot parse HTML. Elements can nest
infinitely, but that would require an infinitely long regular expression,
because they have no mechanism ("stack") to keep track of what they have seen.

For example, `'<div>.*</div>'` (with the `re.DOTALL`/`re.S` flag) will capture
everything in the text below except the final `</div>` tag. There is no way to
pair open tags with their close tags unless they are hardcoded.

```html
<div>The parent div element.
    <div>The child div element.
    </div>
</div>
```

Theoretical background: https://en.wikipedia.org/wiki/Chomsky\_hierarchy
Must-read: https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454

HOWEVER, regular expressions CAN be used to quickly find a relevant part of
HTML.

The BEST way is to use a real HTML parser, which we will do later. However, for
simple jobs, regular expressions are easier to write, and they virtually always
execute faster that HTML parsers.

### Using browser developer tools to explore HTML

* `View Source`
* In Chrome go to `View | Developer > | Developer Tools`

### Using regex to pseudo-parse HTML

In a browser open a webpage:
`https://www.rd.com/jokes/halloween-jokes-for-kids/`
...then View Source, then search for 'Mummy' in the source
each joke is contained in an `<article>` tag
the joke title is inside the `<h3>` tag
the joke itself is inside a `<p>` tag inside a `<div>` tag with `class="content-wrapper`

`PRACTICE 1`
Copy and paste the source html to regex101.com or pythex.org. BE SURE TO SELECT
THE `Python` FLAVOR of REGEX, AND SELECT THE `single line` FLAG! This flag
makes it so that `.` matches newlines, i.e. `.*` can match multiple lines. (In
python code, this is the `re.S` flag)

    * write a regex to capture only the open `<article>` tags with `joke` in the class attribute.
    * write a regular expression to capture all the `<article>`s
    * modify the regex to also capture the title of each joke using a group
    * modify the regex to capture the joke itself, too
    * modify the regex to capture the Q and the A part of the joke separately

### Retrieving a webpage

We can use the requests module to pull the source of a webpage into
a string object.

```python
import requests

joke_url = 'https://www.rd.com/jokes/halloween-jokes-for-kids/'
h = {'user-agent': 'Robert Reynolds (robert_reynolds@byu.edu)'}
response = requests.get(joke_url, headers=h)
print(response.text[:100], '....')  # The HTML source is in the text attribute
```

`PRACTICE 2`
Write a script to pull the html and pseudo-parse it with a regex to extract
the joke titles, the Q and the A. I recommend using `re.findall()`.

### spoofing a browser

Some servers will block your python script purely by virtue of the fact that it
is not a popular browser. If you believe that circumventing this block is still
ethical, this is how you can spoof a browser user-agent.

1. Open a browser of your choice and google `"what is my user agent"`.
1. Copy the result that Google returns into your header dictionary's
    `user-agent`. Add your name and email to the end of the `user-agent` entry.
    * if this still fails, then consider whether it would be ethical to proceed
        without any identifying information. Use generous sleep times, etc.
1. Make http requests as usual.

### Query strings

When you type in `spam` on google.com and hit [return], it pulls up a new page
with a url like this:
https://www.google.com/search?q=spam&oq=spam&aqs=chrome..69i57j0l5.3641j0j8&sourceid=chrome&ie=UTF-8
Everything after the `?` is query strings with the following key/value pairs
separated by ampersands (`&`).

```
q         spam
oq        spam
aqs       chrome..69i57j0l5.3641j0j8
sourceid  chrome
ie        UTF-8
```

***URL escapes***

```python
>>> import urllib.parse
>>> query = 'Hellö Wörld@Python'
>>> urllib.parse.quote(query)
'Hell%C3%B6%20W%C3%B6rld%40Python'
```

You can construct urls inside python to get search results:

```python
import random
import requests as r
import time
from urllib.parse import quote

responses = []
google = 'https://news.google.com/search?q='
for term in ['xkcd', 'tesla', 'Bernie Sanders']:
    responses.append(r.get(google + quote(term), headers=headers))
    time.sleep(2)  # Let the server breathe (2 seconds)
for response in responses:
    print('Do stuff with those websites here...')
```

`NB!` Without `time.sleep()`, the code above would be extremely impolite,
and many servers would immediately block your ip address! It sends requests as
fast as python can function, which can overload a server, and is essentially
what a DDoS attack consists of.
