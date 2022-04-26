
import requests
from bs4 import BeautifulSoup
import csv 					# excell file or woksheet 
from itertools import zip_longest # used to pick item from each list and put them at same index


def search(work,location):

    result = requests.get(f"https://www.indeed.com/jobs?q={work}&l={location}%2C%20PA&radius=100&vjk=8ab7193a2ed408eb")



    src=result.content

    soup=BeautifulSoup(src,"lxml")


    links=[]
    job_titles=soup.find_all("h2",{"class":"jobTitle jobTitle-color-purple"})
    
    for i in range(len(job_titles)):
       links.append(job_titles[i].find("a").attrs['href'])
    print(links)

search("python","lebanon")