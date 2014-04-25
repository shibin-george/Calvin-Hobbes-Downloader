#Author: Shibin George
#This script uses the 3rd - party python library: "BeautifulSoup"
#Please make sure that it is installed in your system

import urllib2
import urllib
from datetime import datetime, date, timedelta
from urllib import FancyURLopener
from bs4 import BeautifulSoup
from random import choice
import os

os.environ['http_proxy']=''
user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
]
#The user-agents above were used because "www.gocomics.com" was blocking
#python urllib2 requests(commonly observed, so as to prevent bulk download/traffic)
#The site is actually blocking the default user agent used by python-urllib2.
#Using a random user-agent from the above list bypasses the issue. Credits: Stackoverflow

start = date(1985, 11, 18)  # <--- modify the start date here
end = date(1985, 11, 30)    # <--- modify the end date here
delta = timedelta(days = 1) #increment in dates

#Calvin and Hobbes is a daily comic strip that was
#written and illustrated by American cartoonist Bill Watterson,
#and syndicated from November 18, 1985, to December 31, 1995

while start <= end:
    s = str(start)
    date = s[0:4] + "/" + s[5:7] + "/" + s[8:] + "/"
    s = s[0:4] + "_" + s[5:7] + "_" + s[8:]
    print "\nIssue Date: " + date
    url = "http://www.gocomics.com/calvinandhobbes/" + date
    print  "Requesting: \" " + url + " \""

    headers = {'User-Agent':choice(user_agents)}
    req = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(req)
    page = response.read()
    soup = BeautifulSoup(page)
    
    i=0
    for image in soup.find_all('img'):  #search for img tags
        i = i+1
        if(i==3):
            #The third img tag contains the link to the Calvin&Hobbes comic strip,
            #found it after a bit of experimentation   
            img_link = image['src'] #extracts  the "src" attribute from the tag
            break

    print "Downloading C&H for " + date + " from \"" + img_link + "\""
    image = urllib2.urlopen(img_link)
    filename = "/host/Calvin&Hobbes/CnH" + s + ".jpg"
    file = open(filename, "wb")
    file.write(image.read())
    file.close()
    
    #uncomment the below line to view the page content
    #print soup.prettify()
    start += delta    #proceed to the next date

print "\nCalvin&Hobbes downloaded. Thanks for reviewing/using this script."
    
    
