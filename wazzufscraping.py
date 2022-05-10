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

def search_wazzuf(work):
    counter=0
    #2nd step use requests to fetch the url and get the page 
    result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q={work}")




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
    links=[]


    for i in range(len(job_titles)):
       job_title.append(job_titles[i].text)
       links.append("https://wuzzuf.net"+job_titles[i].find("a").attrs['href'])
       company_name.append(company_names[i].text)
       location_name.append(location_names[i].text)
       skills.append(job_skills[i].text)

    # print(job_title)
    # print(company_name)
    # print(location_name)
    # print(skills)

    #7th create csv file and fill it with texts
    file_list=[job_title,company_name,location_name,skills,links]
    exported=zip_longest(*file_list)
    #what happen ????????example :
    #x=[1,2,3]
    #y=['a','b','c']
    #z=[x,y]
    #*z------>[[1,2,3],["a","b","c"]]
    #zip_longest(*z)---->[1,a][2,b][3,c]
    #this will help us in using writerows function.

    with open(f"C:/Users/User/Desktop/web_scraping/data/{work}.csv","w") as myfile:#open create file if not found,w=write mode
        #now we use csv module that help to contact with csv file
        wr=csv.writer(myfile)
        wr.writerow(["job title","company name","location","skills","links",])
        wr.writerows(exported)



    #################################################


    result1 = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q={work}&start=1")


    #3rd step save page content/markup (just contents and words)
    src=result1.content
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
    links=[]


    for i in range(len(job_titles)):
       job_title.append(job_titles[i].text)
       links.append("https://wuzzuf.net"+job_titles[i].find("a").attrs['href'])
       company_name.append(company_names[i].text)
       location_name.append(location_names[i].text)
       skills.append(job_skills[i].text)

    # print(job_title)
    # print(company_name)
    # print(location_name)
    # print(skills)

    #7th create csv file and fill it with texts
    file_list=[job_title,company_name,location_name,skills,links]
    exported=zip_longest(*file_list)
    #what happen ????????example :
    #x=[1,2,3]
    #y=['a','b','c']
    #z=[x,y]
    #*z------>[[1,2,3],["a","b","c"]]
    #zip_longest(*z)---->[1,a][2,b][3,c]
    #this will help us in using writerows function.

    with open(f"C:/Users/User/Desktop/web_scraping/data/{work}.csv","a") as myfile:#open create file if not found,w=write mode
        #now we use csv module that help to contact with csv file
        wr=csv.writer(myfile)
        wr.writerows(exported)




    result1 = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q={work}&start=2")


    #3rd step save page content/markup (just contents and words)
    src=result1.content
    # print(src)


     

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
    links=[]


    for i in range(len(job_titles)):
       job_title.append(job_titles[i].text)
       links.append("https://wuzzuf.net"+job_titles[i].find("a").attrs['href'])
       company_name.append(company_names[i].text)
       location_name.append(location_names[i].text)
       skills.append(job_skills[i].text)

    # print(job_title)
    # print(company_name)
    # print(location_name)
    # print(skills)

    #7th create csv file and fill it with texts
    file_list=[job_title,company_name,location_name,skills,links]
    exported=zip_longest(*file_list)
   

    with open(f"C:/Users/User/Desktop/web_scraping/data/{work}.csv","a") as myfile:#open create file if not found,w=write mode
        #now we use csv module that help to contact with csv file
        wr=csv.writer(myfile)
        wr.writerows(exported)





    result1 = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q={work}&start=3")


    #3rd step save page content/markup (just contents and words)
    src=result1.content
    # print(src)


     

    soup=BeautifulSoup(src,"lxml")




    job_titles=soup.find_all("h2",{"class":"css-m604qf"})#first param is link tags , and second is dectionary  to filter link tags we want.
    #find all will return list
    # print(job_titles)
    company_names=soup.find_all("a",{"class":"css-17s97q8"})
    # print(company_name)
    location_names=soup.find_all("span",{"class":"css-5wys0k"})
    # print(location_names)
    job_skills=soup.find_all("div",{"class":"css-y4udm8"})

    job_title=[]
    company_name=[]
    location_name=[]
    skills=[]
    links=[]


    for i in range(len(job_titles)):
       job_title.append(job_titles[i].text)
       links.append("https://wuzzuf.net"+job_titles[i].find("a").attrs['href'])
       company_name.append(company_names[i].text)
       location_name.append(location_names[i].text)
       skills.append(job_skills[i].text)
   
    file_list=[job_title,company_name,location_name,skills,links]
    exported=zip_longest(*file_list)


    with open(f"C:/Users/User/Desktop/web_scraping/data/{work}.csv","a") as myfile:#open create file if not found,w=write mode
        #now we use csv module that help to contact with csv file
        wr=csv.writer(myfile)
        wr.writerows(exported)





    result1 = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q={work}&start=6")



    src=result1.content


    soup=BeautifulSoup(src,"lxml")


    job_titles=soup.find_all("h2",{"class":"css-m604qf"})#first param is link tags , and second is dectionary  to filter link tags we want.
    #find all will return list
    # print(job_titles)
    company_names=soup.find_all("a",{"class":"css-17s97q8"})
    # print(company_name)
    location_names=soup.find_all("span",{"class":"css-5wys0k"})
    # print(location_names)
    job_skills=soup.find_all("div",{"class":"css-y4udm8"})


    job_title=[]
    company_name=[]
    location_name=[]
    skills=[]
    links=[]


    for i in range(len(job_titles)):
       job_title.append(job_titles[i].text)
       links.append("https://wuzzuf.net"+job_titles[i].find("a").attrs['href'])
       company_name.append(company_names[i].text)
       location_name.append(location_names[i].text)
       skills.append(job_skills[i].text)

  
    file_list=[job_title,company_name,location_name,skills,links]
    exported=zip_longest(*file_list)


    with open(f"C:/Users/User/Desktop/web_scraping/data/{work}.csv","a") as myfile:#open create file if not found,w=write mode
        #now we use csv module that help to contact with csv file
        wr=csv.writer(myfile)
        wr.writerows(exported)





    result1 = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q={work}&start=7")


    #3rd step save page content/markup (just contents and words)
    src=result1.content
    # print(src)


     

    soup=BeautifulSoup(src,"lxml")

    job_titles=soup.find_all("h2",{"class":"css-m604qf"})#first param is link tags , and second is dectionary  to filter link tags we want.
    #find all will return list
    # print(job_titles)
    company_names=soup.find_all("a",{"class":"css-17s97q8"})
    # print(company_name)
    location_names=soup.find_all("span",{"class":"css-5wys0k"})
    # print(location_names)
    job_skills=soup.find_all("div",{"class":"css-y4udm8"})
    # print(job_skills)

    job_title=[]
    company_name=[]
    location_name=[]
    skills=[]
    links=[]


    for i in range(len(job_titles)):
       job_title.append(job_titles[i].text)
       links.append("https://wuzzuf.net"+job_titles[i].find("a").attrs['href'])
       company_name.append(company_names[i].text)
       location_name.append(location_names[i].text)
       skills.append(job_skills[i].text)


    file_list=[job_title,company_name,location_name,skills,links]
    exported=zip_longest(*file_list)

    with open(f"C:/Users/User/Desktop/web_scraping/data/{work}.csv","a") as myfile:#open create file if not found,w=write mode
        #now we use csv module that help to contact with csv file
        wr=csv.writer(myfile)
        wr.writerows(exported)



    result1 = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q={work}&start=8")


    src=result1.content



    soup=BeautifulSoup(src,"lxml")



    job_titles=soup.find_all("h2",{"class":"css-m604qf"})
    #find all will return list
    # print(job_titles)
    company_names=soup.find_all("a",{"class":"css-17s97q8"})
    # print(company_name)
    location_names=soup.find_all("span",{"class":"css-5wys0k"})
    # print(location_names)
    job_skills=soup.find_all("div",{"class":"css-y4udm8"})
    # print(job_skills)

    job_title=[]
    company_name=[]
    location_name=[]
    skills=[]
    links=[]


    for i in range(len(job_titles)):
       job_title.append(job_titles[i].text)
       links.append("https://wuzzuf.net"+job_titles[i].find("a").attrs['href'])
       company_name.append(company_names[i].text)
       location_name.append(location_names[i].text)
       skills.append(job_skills[i].text)


    file_list=[job_title,company_name,location_name,skills,links]
    exported=zip_longest(*file_list)

    with open(f"C:/Users/User/Desktop/web_scraping/data/{work}.csv","a") as myfile:
        wr=csv.writer(myfile)
        wr.writerows(exported)
        


    result1 = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q={work}&start=9")


    src=result1.content



    soup=BeautifulSoup(src,"lxml")



    job_titles=soup.find_all("h2",{"class":"css-m604qf"})
    #find all will return list
    # print(job_titles)
    company_names=soup.find_all("a",{"class":"css-17s97q8"})
    # print(company_name)
    location_names=soup.find_all("span",{"class":"css-5wys0k"})
    # print(location_names)
    job_skills=soup.find_all("div",{"class":"css-y4udm8"})
    # print(job_skills)

    job_title=[]
    company_name=[]
    location_name=[]
    skills=[]
    links=[]


    for i in range(len(job_titles)):
       job_title.append(job_titles[i].text)
       links.append("https://wuzzuf.net"+job_titles[i].find("a").attrs['href'])
       company_name.append(company_names[i].text)
       location_name.append(location_names[i].text)
       skills.append(job_skills[i].text)


    file_list=[job_title,company_name,location_name,skills,links]
    exported=zip_longest(*file_list)

    with open(f"C:/Users/User/Desktop/web_scraping/data/{work}.csv","a") as myfile:
        wr=csv.writer(myfile)
        wr.writerows(exported)

   
        
        



if __name__=="__main__":
    print(__doc__)
