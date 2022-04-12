"""
first step you need to install and import modules :
 requests
 beautifullsoup4
"""
import requests
from bs4 import BeautifulSoup
import csv 					# excell file or woksheet 
from itertools import zip_longest



#2nd step use requests to fetch the url and get the page 
result = requests.get("https://wuzzuf.net/search/jobs/?a=hpb&q=python")




#3rd step save page content/markup (just contents and words)
src=result.content
print(src)





#4th step create soup object to parse content
#to get useful information from the content
#src = page we want to take from it information
#parser =helps us to make processing on the page
soup=BeautifulSoup(src,"lxml")



#5th step find the elements containing info we need
#job titles, job skills ,company names; location names

