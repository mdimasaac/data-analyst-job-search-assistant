#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup as bs4
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import getpass
import easygui as eg
from tqdm import tqdm


# In[2]:


def click(x):
    button = driver.find_element(By.XPATH, x)
    button.click()
    time.sleep(2)


# ### scraping from stepstone

# scraping from stepstone.de to get page source of the job results pages (page 1, page 2, page 3, etc.)

# In[3]:


def scrape_pages(url):
    search_result = []
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('user-agent=fake-useragent')
    driver.get(url)
    time.sleep(6)
    ok1 = "/html/body/div[10]/section/div/section/div[2]/div[1]/div[2]/div"
    ok2 = "/html/body/div[9]/section/div/section/div[2]/div[1]/div[2]/div"
    ok3 = "/html/body/div[10]/section/div/section/div[2]/div[1]/div[2]"
    try:
        click(ok1)
    except:
        pass
    try:
        click(ok2)
    except:
        pass
    try:
        click(ok3)
    except:
        pass
    npage = "/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[3]/div/nav/ul/li[9]/a"
    html = driver.page_source
    a = 0
    while a<20:
        search_result.append(html)
        time.sleep(1)
        i = 0
        while i < 4:
            driver.execute_script("window.scrollTo(0, window.scrollY + 1500)") 
            time.sleep(.2)
            i+=1
        time.sleep(4)
        click(npage)
        html = driver.page_source
        a += 1
    return search_result


# In[4]:


search_result_1 = []


# In[5]:


urls = ["https://www.stepstone.de/jobs/python-data-analyst","https://www.stepstone.de/jobs/sql-data-analyst","https://www.stepstone.de/jobs/tableau-data-analyst","https://www.stepstone.de/jobs/tableau-business-intelligence"]


# In[11]:


driver = webdriver.Chrome(ChromeDriverManager().install())
search_result_1.extend(scrape_pages(urls[3]))


# In[12]:


job_url_1 = []
for h in tqdm(search_result_1):
    soup = bs4(h)
    res = soup.find_all("article",{"class":"resultlist-1jx3vjx"})
    for r in res:
        href = r.find("a",{"class":"resultlist-1uvdp0v"}).get("href")
        href = "https://www.stepstone.de"+href
        job_url_1.append(href)
df_1 = pd.DataFrame(columns = ["job_url"])
df_1["job_url"] = job_url_1


# In[13]:


df_1 = df_1.drop_duplicates(subset = "job_url").reset_index(drop = True)


# In[14]:


# df_1.to_csv("job url 1.csv", index = False)


# In[15]:


# df_1 = pd.read_csv("job url 1.csv")


# In[20]:


def get_page_source(df_url):
    source = []
    job_url = df_url["job_url"].tolist()
    options = Options()
    # installing chromedriver, so that we dont need to keep the chromedriver file
    # that needs to be updated every once in a while. better install the latest automatically
    driver = webdriver.Chrome(ChromeDriverManager().install())
    for i in job_url: # get full page source for each job offer page
        # options.add_argument("--disable-notifications")
        # to prevent from being spotted as a robot
        options.add_argument('--disable-gpu')
        options.add_argument('user-agent=fake-useragent')
        # opens the browser, maximize window size
        # opening url
        driver.get(i)
        time.sleep(3.5)
        page = driver.page_source
        source.append(page)
    # saving source column separately for each splitted file
    job_source = pd.DataFrame(columns = ["job_source"])
    job_source["job_source"] = source
    filename = "job source 1.csv"
    job_source.to_csv(filename, index = False)
    return job_source


# In[21]:


source = get_page_source(df_1)


# getting some details from each page source we had from the big scraping job (see cell above)

# In[51]:


df_stepstone = pd.DataFrame()
url_1,d_1,t_1,cn_1,cl_1,c_1= [],[],[],[],[],[]

df1 = df_1.copy()
df2 = source.copy()
description_1,title_1,comp_name_1,comp_url_1,city_1 = [],[],[],[],[]
source = df2["job_source"].tolist()
for s in source:
    soup = bs4(s, "html.parser")
    try:
        jobtitle = soup.find("span",{"data-at":"header-job-title"}).text
    except:
        jobtitle = "unknown"
    title_1.append(jobtitle)
    try:
        compname = soup.find("a",{"data-at":"header-company-name"}).text
    except:
        compname = "unknown"
    comp_name_1.append(compname)
    try:
        complink = soup.find("a",{"data-at":"header-company-name"}).get("href")
    except:
        complink = "unknown"
    comp_url_1.append(complink)
    try:
        city = soup.find("span",{"class":"listing-content-provider-1u79rpn"}).text
    except:
        city = "unknown"
    city_1.append(city)
    infotext = soup.find_all("div",{"class":"listing-content-provider-10ltcrf"})
    desc = []
    for i in infotext:
        try:
            texts = i.find_all("p")
            for t in texts:
                info = t.text
                desc.append(info)
        except:
            pass
        try:
            texts = i.find_all("li")
            for t in texts:
                info = t.text
                desc.append(info)
        except:
            pass
    # enemy spotted
    description = " ".join(desc).replace("\xa0","").replace("\\n","")
    description_1.append(description)
d_1.extend(description_1)
t_1.extend(title_1)
cn_1.extend(comp_name_1)
cl_1.extend(comp_url_1)
c_1.extend(city_1)
url_1.extend(df1["job_url"].tolist())


# In[53]:


df_stepstone["job_url"] = url_1
df_stepstone["description"] = d_1
df_stepstone["job_title"] = t_1
df_stepstone["comp_name"] = cn_1
df_stepstone["comp_link"] = cl_1
df_stepstone["city"] = c_1


# In[57]:


df_stepstone = df_stepstone[df_stepstone["description"] != ""]


# In[58]:


import numpy as np


# In[60]:


df_stepstone.to_csv("stepstone 1 incomplete.csv", index = False)


# ### now scrape from indeed.com

# In[3]:


from selenium.webdriver.common.keys import Keys


# In[14]:


def scrape_indeed(key):    
    url2 = "https://de.indeed.com/?r=us"
    options = Options()
    # options.add_argument("--disable-notifications")
    # to prevent from being spotted as a robot
    options.add_argument('--disable-gpu')
    options.add_argument('user-agent=fake-useragent')
    # opening url
    driver.get(url2)
    time.sleep(2)
    search_xpath = "/html/body/div[1]/div[1]/div/span/div[4]/div[2]/div/div/div/div/form/div/div[1]/div/div[1]/div/div[2]/input"
    search = driver.find_element(By.XPATH,search_xpath)

    search.send_keys(key)
    findjob_xpath = "/html/body/div[1]/div[1]/div/span/div[4]/div[2]/div/div/div/div/form/button"
    click(findjob_xpath)

    html = driver.page_source
    npage = "/html/body/main/div/div[1]/div/div/div[5]/div[1]/nav/div[6]/a"
    lhtml2 = []
    counter = 1
    a = 0
    while a < 30:
        if counter == 2:
            time.sleep(2)
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        lhtml2.append(html)
        time.sleep(1)
        i = 0
        while i < 4:
            driver.execute_script("window.scrollTo(0, window.scrollY + 1500)") 
            time.sleep(.2)
            i+=1
        time.sleep(1)
        try:
            click(npage)
        except:
            a = 30
        counter += 1
        html = driver.page_source
        # comparing html_before and html_after
        a += 1
    return lhtml2


# In[15]:


keys = ["sql data analyst","python data analyst","tableau data analyst","tableau business intelligence"]
driver = webdriver.Chrome(ChromeDriverManager().install())
lhtml2 = []
for key in keys:
    lhtml2.extend(scrape_indeed(key))


# In[16]:


lhref2 = []
for h in tqdm(lhtml2):
    soup = bs4(h)
    container = soup.find("ul",{"class":"jobsearch-ResultsList css-0"})
    res = container.find_all("div",{"class":"slider_container css-g7s71f eu4oa1w0"})
    for r in res:
        href = r.find("h2",{"tabindex":"-1"}).find("a").get("href")
        href = "https://de.indeed.com" + href
        lhref2.append(href)
href_pd2 = pd.DataFrame(columns = ["job_url"])
href_pd2["job_url"] = lhref2


# In[20]:


source2 = []
options = Options()
# installing chromedriver, so that we dont need to keep the chromedriver file
# that needs to be updated every once in a while. better install the latest automatically
driver = webdriver.Chrome(ChromeDriverManager().install())
for i in tqdm(lhref2):
    # options.add_argument("--disable-notifications")
    # to prevent from being spotted as a robot
    options.add_argument('--disable-gpu')
    options.add_argument('user-agent=fake-useragent')
    # opening url
    driver.get(i)
    time.sleep(3)
    page = driver.page_source
    source2.append(page)
href_pd2["job_source"] = source2


# In[21]:





# In[22]:


ldescription2,ltitle2,lcompname2,lcomplink2,lcity2 = [],[],[],[],[]

for s in tqdm(source2):
    soup = bs4(s, "html.parser")
    try:
        jobtitle = soup.find("h1",{"class":"icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title"}).text
    except:
        jobtitle = None
    ltitle2.append(jobtitle)
    try:
        compname = soup.find("div",{"data-company-name":"true"}).text
    except:
        compname = None
    lcompname2.append(compname)
    try:
        complink = soup.find("div",{"data-company-name":"true"}).find("a").get("href")
    except:
        complink = None
    lcomplink2.append(complink)
    city = None
    lcity2.append(city)
    infotext = soup.find("div",{"id":"jobDescriptionText"}).find_all("p")
    desc = []
    for i in infotext:
        try:
            texts = i.find("b").text
            desc.append(texts)
        except:
            texts = i.text
        desc.append(texts)
    # enemy spotted
    description = " ".join(desc)
    ldescription2.append(description)


# In[23]:


href_pd2["description"] = ldescription2
href_pd2["job_title"] = ltitle2
href_pd2["comp_name"] = lcompname2
href_pd2["comp_link"] = lcomplink2
href_pd2["city"] = lcity2
href_pd2.to_csv("indeed 1 incomplete.csv", index = False)


# In[24]:


href_pd2 = pd.read_csv("indeed 1 incomplete.csv")


# In[27]:


href_pd = pd.read_csv("stepstone 1 incomplete.csv")


# In[36]:


full = pd.concat([href_pd, href_pd2], axis = 0)


# In[37]:


full = full[full["description"] != ""]
full = full.drop(columns = ["job_source"])


# In[38]:


full.to_csv("full.csv", index = False)
df = full.copy()


# In[ ]:


df = df.dropna(subset = ["comp_link"])


# In[ ]:


querying = ["data","analy","analy","sql","sql","sql","big data","query","entry","base","warehouse"] #A
engineering = ["python","python","data","analy","analy","machine","learn","etl","oop","pipe","pipe","tensor","engineer","nlp"] #B
analysis = ["python","python","python","data","analy","analy","eda","predict","machine","learn","test","explor","statisti"] #C
model_building = ["python","python","data","analy","analy","machine","machine","learn","predict","ml","model","model","train"] #D
scraping = ["python","python","python","data","analy","analy","clean","mining","scrap","csv","json","api"] #E
dashboarding = ["bi","bi","power","data","analy","analy","dashboard","tableau","tableau","tableau","report","visuali"] #F
category = [querying, engineering, analysis, model_building, scraping, dashboarding]


# In[ ]:


A,B,C,D,E,F = [],[],[],[],[],[]

scores = [A,B,C,D,E,F]
description = df.description.tolist()
for des in tqdm(description):
    for score, cat in list(zip(scores, category)):
        sc = []
        for i in cat:
            if i in str(des).lower():
                sc.append(1)
            # else:
            #     sc.append(0)
        n = len(sc)/len(cat)*100
        score.append(round(n,2))        


# In[ ]:


df["querying"] = A
df["engineering"] = B
df["analysis"] = C
df["model_building"] = D
df["scraping"] = E
df["dashboarding"] = F
df = df.fillna("unknown")


# In[ ]:


city = []
for i in df["city"]:
    if "," in i:
        i= "multiple cities"
        city.append(i)
    else:
        city.append(i)
df["city"] = city


# In[ ]:


X = df.drop(columns=["job_url","description","comp_link"])
df.to_csv("data clean with url.csv", index = False)
X.to_csv("data clean.csv", index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




