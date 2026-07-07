# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count = int(raw_input(' Enter count'))
pos =  int (raw_input('enter position'))

for i in range(0,count):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	# Retrieve all of the anchor tags
	tags = soup('a')
	url=tags[pos-1].get('href',None)
	print url


