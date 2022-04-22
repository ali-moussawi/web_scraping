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
# print(src)


 


#4th step create soup object to parse content
#to get useful information from the content
#src = content we want to take from it information
#parser lxml =helps us to make processing on the page
soup=BeautifulSoup(src,"lxml")



#5th step find the elements containing info we need
#job titles, job skills ,company names; location names
#all information are inside html tags.
job_titles=soup.find_all("h2",{"class":"css-m604qf"})#first param is link tags , and second is dectionary  to filter link tags we want.
#find all will return list
# print(job_titles)
company_names=soup.find_all("a",{"class":"css-17s97q8"})
# print(company_name)
location_names=soup.find_all("span",{"class":"css-5wys0k"})
# print(location_names)
job_skills=soup.find_all("div",{"class":"css-y4udm8"})
# print(job_skills)

# 6th loop over returned list to extract texts inside it
#make list to save this text inside it
job_title=[]
company_name=[]
location_name=[]
skills=[]



for i in range(len(job_titles)):
   job_title.append(job_titles[i].text)
   company_name.append(company_names[i].text)
   location_name.append(location_names[i].text)
   skills.append(job_skills[i].text)


# print(job_title)
# print(company_name)
# print(location_name)
# print(skills)

#7th create csv file and fill it with texts
file_list=[job_title,company_name,location_name,skills]
exported=zip_longest(*file_list)
#what happen ????????example :
#x=[1,2,3]
#y=['a','b','c']
#z=[x,y]
#*z------>[[1,2,3],["a","b","c"]]
#zip_longest(*z)---->[1,a][2,b][3,c]
#this will help us in using writerows function.

with open("C:/Users/User/Desktop/web_scraping/data/data.csv","w") as myfile:#open create file if not found,w=write mode
    #now we use csv module that help to contact with csv file
    wr=csv.writer(myfile)
    wr.writerow(["job title","company name","location","skills"])
    wr.writerows(exported)



#8 now there is more privacey information that need to get inside each job to fetch it like salary time
#so there is link that take us for each job
#this link is inside h2 stored inside job_titles
# so now i can make loop inside job_titles that contains links and use method find to fetch just the links
#jobtitle=[title1,title2.....]
links=[]
for i in range(len(job_titles)):
  
    links.append(job_titles[i].find("a").attrs['href'])


# now i get all the links 
salary=[]
for link in links:
    result=requests.get("https://wuzzuf.net/jobs/p/ItXgcrG6BIJb-Python-Developer-FlairsTech-Cairo-Egypt?o=1&l=sp&t=sj&a=python|search-v3|navbg")
    src=result.content
    soup=BeautifulSoup(src,"lxml")
    salaries=soup.find_all("span",{"class":"css-4xky9y"})
    print(salaries)
    break;


