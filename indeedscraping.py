"""
our project aimed to make a script on a target job website to get a needed data about a jobs without wasting our time seeing ads, scrolling up and down etc..
so in order to achieve ou target  we use 4 modules
1st requests = give it url to get all content about the website page provided by the url
2nd BeautifulSoup = this module used to control the data or content gathered by the request module
 it is a python library for pulling data out of HTML and XML files. It creates data parse trees in order to get data easily.
3rd csv = used to work with the excell or work sheet in order to write, read data from them
4th itertools = it gives very usefull tools that help you in dealing with lists and comine them in the way you need
5th tkinter = its a gui module that pretty our app and gives a user interface veiw

In computer technology, a parser is a program, usually part of a compiler,
 that receives input in the form of sequential source program instructions, interactive online commands, markup tags, 
 or some other defined interface and breaks them up into parts (for example, the nouns (objects), verbs (methods), a
 nd their attributes or options) that can then be managed by other programming 
 (for example, other components in a compiler).
 A parser may also check to see that all input has been provided that is necessary.
"""
import requests
from bs4 import BeautifulSoup
import csv 					# excell file or woksheet 
from itertools import zip_longest # used to pick item from each list and put them at same index


def search_indeed(work,location="lebanon"):
    count=10
    while(count<11):
        result = requests.get(f"https://www.indeed.com/jobs?q={work}&l={location}&start={count}")
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

        file_list=[titles,links]
        exported=zip_longest(*file_list)

        for i in (range(len(links))):
            result1=requests.get(links[i])
            src1=result1.content
            soup1=BeautifulSoup(src1,"lxml")
            ### find titles
            titles.append(soup1.find("h1",{"class":"icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title"}).text)



        with open(f"C:/Users/User/Desktop/web_scraping/data/{work}_indeed.csv","w") as myfile:#open create file if not found,w=write mode
            #now we use csv module that help to contact with csv file
            wr=csv.writer(myfile)
            wr.writerow(["job title","links",])
            wr.writerows(exported)

        count+=10

if __name__=="__main__":
    print(__doc__)
