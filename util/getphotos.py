from BeautifulSoup import BeautifulSoup
import urllib2
import re
from urllib import urlretrieve


for number in range(1,11): 

	print 'opening: ', 'http://numberoftheday.co.uk/tagged/%s' % number

	u = urllib2.urlopen('http://numberoftheday.co.uk/tagged/%s' % number)
	html = BeautifulSoup(u)
	
	ctr = 0
	for photodiv in html.findAll('div', attrs={'class' : 'photo'}):
		src = photodiv.find('img')['src']
		filename = src.split("/")[-1]
		extension = filename.split(".")[-1]
		if extension.lower() == "jpg":			
			print src
			ctr += 1
			urlretrieve(src, '../www/resources/images/numbers/%s/%s.jpg' % (number, ctr))

# print html