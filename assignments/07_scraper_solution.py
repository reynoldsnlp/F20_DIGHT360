"""Scrape information from a webpage."""

import re

import requests


# get content from website
peanut_butter_url = 'https://www.today.com/food/best-peanut-butters-according-nutritionists-chefs-t145189'
h = {'user-agent': 'Devon Su (devonleoc@gmail.com)'}
response = requests.get(peanut_butter_url, headers=h)
the_response = response.text

# write html source to peanut_butter.html
with open('peanut_butter.html', 'w') as html_file:
    print(the_response, file=html_file)

# read peanut_butter.html as a string
with open('peanut_butter.html', 'r') as html_file:
    data = html_file.read()

# use regex to parse string
regex = r'<h2 class="">(\d+.).*?<a.*?>(.*?)</a>.*?sp.*?b">(\$).*?>(\d.\d+)'
filter = re.findall(regex, data, flags=re.IGNORECASE)

# write parsed info to a txt file
with open('peanut_butter_parsed.txt', 'w') as outfile:
    for a, b, c, d in filter:
        print(a, b, c + d, file=outfile)
