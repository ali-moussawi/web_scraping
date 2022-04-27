
import requests
from bs4 import BeautifulSoup
import csv 					# excell file or woksheet 
from itertools import zip_longest # used to pick item from each list and put them at same index


def search(work,location):

    result = requests.get(f"https://www.indeed.com/jobs?q={work}&l={location}")
    src=result.content
    soup = BeautifulSoup(src, 'html.parser')

    job_titles=soup.find_all("h2",{"class":"jobTitle jobTitle-color-purple"})
    # print(job_titles)
    links=[]
    

    for i in (range(len(job_titles))):
        index =job_titles[i].find('a').attrs['href']
        char=index.index('?')
        newlink="https://www.indeed.com/viewjob"+index[char:]
        links.append(newlink)
    # print(links)
    titles=[]
    salary=[]
    location=[]
    requirements=[]

    for i in (range(len(links))):
        result1=requests.get(links[i])
        src1=result1.content
        soup1=BeautifulSoup(src1,"lxml")
        ### find titles
        titles.append(soup1.find("h1",{"class":"icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title"}).text)
        ### find salary
        salaryul=soup1.find("ul",{"class":"css-1lyr5hv eu4oa1w0"})






    print(salaryul)
    # print(titles)






search("Cashier","lebanon")