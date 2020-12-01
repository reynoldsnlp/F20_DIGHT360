# Selenium (automate your browser using python)

## Installation

http://selenium-python.readthedocs.io/installation.html

$ python3 -m pip install --user selenium

Download driver:
    * http://selenium-python.readthedocs.io/installation.html#drivers
    * Save the driver in one of the folders in your PATH variable
      (/usr/local/bin/ or /usr/bin/ are reasonable places on MacOS or Linux)
      * ...or just save it in the same folder as your selenium script.

## Example

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# if chromedriver is not in your PATH, put the absolute path to it as an
# argument to Chrome()
# driver = webdriver.Chrome('/path/to/my/chromedriver')  # MacOS/Linux
# driver = webdriver.Chrome(r'C:\path\to\my\chromedriver')  # Windows
driver = webdriver.Chrome()
driver.get("http://www.python.org")  # does not necessarily wait for AJAX
assert "Python" in driver.title
# see https://selenium-python.readthedocs.io/locating-elements.html
elem = driver.find_element_by_name("q")
print('elem:', type(elem), elem)
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print(driver.page_source[:200], '....')
assert "No results found." not in driver.page_source
input('Press [return] to close Chrome driver.')
driver.close()
```

`PRACTICE A`

Install selenium and run this script.

`PRACTICE B`

Write a script to get `http://reynoldsnlp.com/scrape/aa.html` and save the
source html to a local file.

## Locating elements

Selenium (and BeautifulSoup for that matter) allow you to use many ways to
locate elements in an html tree. (See
http://selenium-python.readthedocs.io/locating-elements.html for a list of the
selenium functions and scroll down for examples of how to use each one.)

Using Xpath or css selectors to find an element is usually a last resort,
because they are brittle against any tiny changes to the website. Your script
will likely break sooner than later. However, if you do need to use Xpath or
css selectors, the `Developer Tools` of your browser are extremely helpful. In
the `Elements` tab (viewing the html source of the displayed page), just
right-click on an element, hover over `Copy`, then select `Copy selector`,
`Copy Xpath`, or `Copy Full Xpath`. Then paste the selector or Xpath as an
argument to `find_element_by_css_selector` or `find_element_by_xpath`.

`PRACTICE C`

Write a script to open `https://www.google.com` and search for
`selenium-python tutorial`. Print the contents of each `<cite>` tag.
(see http://selenium-python.readthedocs.io/locating-elements.html)

## Scraping twitter

Currently, many of the popular python libraries for scraping twitter are
broken.  One example that I found of someone with a working script is
[here](https://github.com/theo-go/twitter_selenium_get_tweets) under an MIT
license, so you can copy and use this however you want. You will probably need
to customize the script to fit your needs.
