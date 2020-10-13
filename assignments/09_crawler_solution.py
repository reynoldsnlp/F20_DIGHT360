"""Iteratively scrape reynoldsnlp.com/scrape/."""

from glob import glob
import os
import sys
import time

from bs4 import BeautifulSoup
import requests

try:
    os.mkdir('scrape')  # Create the `scrape` directory
except FileExistsError:
    pass  # If it already exists, do nothing


def get_reynoldsnlp(filename):
    """Scrape html file from reynoldsnlp.com/scrape/; write to file."""
    # time.sleep(1)
    print('Requesting {}....'.format(filename), file=sys.stderr)
    headers = {'user-agent': 'Robert Reynolds (robert_reynolds@byu.edu)'}
    req = requests.get('http://reynoldsnlp.com/scrape/' + filename,
                       headers=headers)
    with open('scrape/' + filename, 'w') as html_file:
        html_file.write(req.text)


def get_hrefs(filename):
    """Return list of href values from all <a> tags in `filename`."""
    assert filename.endswith('.html')
    print('Extracting hrefs from {}....'.format(filename), file=sys.stderr)
    with open('scrape/' + filename) as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
    return [link['href'].split('/')[-1]
            for link in soup.find_all('a')
            if 'reynoldsnlp.com/scrape' in link['href']]
    # or as a for loop...
    # output_list = []
    # for link in soup.find_all('a'):
    #     if 'reynoldsnlp.com/scrape' in link['href']:
    #         output_list.append(link['href'].split('/')[-1])
    # return output_list


todo = {'aa.html'}  # seed url
done = set()
while todo:
    fname = todo.pop()
    get_reynoldsnlp(fname)
    new_hrefs = get_hrefs(fname)
    for new_href in new_hrefs:
        if new_href not in done:
            todo.add(new_href)
    # this for loop could be replaced with the following line
    # todo.update({h for h in new_hrefs if h not in done})
    done.add(fname)

names = sorted([u.split('/')[-1][:2] for u in glob('scrape/*.html')])
print(len(names), names)
# We are missing fa.html
