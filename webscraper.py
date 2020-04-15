# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 02:39:59 2019

@author: Saurabh Gupta
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




link=[] 
name=[] 
ratings=[] 
amenities = []
reviews = []
nofreviews = []
hostname = []
hostjoiningdate = []
host_nreviews = []
host_languages = []
response_rate = []
response_time = []
verification = []
host_review = []
host_link = []



def getsoup(link):
    options = webdriver.FirefoxOptions()
    options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
    driver = webdriver.Firefox(options=options, executable_path="C:/Utility/BrowserDrivers/geckodriver.exe")
    driver.get(link)
    wait = WebDriverWait(driver, 7)
    wait.until(EC.visibility_of_element_located((By.ID, "amenities")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_4xosax")))
    wait.until(EC.visibility_of_element_located((By.ID, "reviews")))
    wait.until(EC.visibility_of_element_located((By.ID, "host-profile")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_1p0spma2")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_czm8crp")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_1ij6gln6")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_10ejfg4u")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_rqfxvmb")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_1p3joamp")))
    #driver.get('https://www.airbnb.co.in/rooms/22825904?location=California%2C%20United%20States&adults=1&check_in=2020-01-30&check_out=2020-01-31&source_impression_id=p3_1576496294_zBD%2Bb8fdiCQHjjXr')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    content = driver.page_source
    time.sleep(2)
    driver.close()
    soup = BeautifulSoup(content,'html.parser')
    return soup

def getsssoup(link):
    options = webdriver.FirefoxOptions()
    options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
    driver = webdriver.Firefox(options=options, executable_path="C:/Utility/BrowserDrivers/geckodriver.exe")
    driver.get(link)
    wait = WebDriverWait(driver, 7)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_2h22gn")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_czm8crp")))
    #driver.get('https://www.airbnb.co.in/rooms/22825904?location=California%2C%20United%20States&adults=1&check_in=2020-01-30&check_out=2020-01-31&source_impression_id=p3_1576496294_zBD%2Bb8fdiCQHjjXr')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    content = driver.page_source
    time.sleep(2)
    driver.close()
    soup = BeautifulSoup(content,'html.parser')
    return soup

def getamenities(soup):
    amens = []
    for a in soup.findAll('div', attrs = {'id' : 'amenities'}):
        print('hello')
        
        for b in a.findAll('td', attrs = {'class' : '_4xosax'}):
            amen = b.text
            amens.append(amen)
    return (amens)

def getnreviews(soup):
    for a in soup.findAll('div', attrs = {'id' : 'reviews'}):
        print('hello1')
        for b in a.findAll('span', attrs = {'class' : '_1p0spma2'}):
            return(b.text)
        
def getreviews(soup):
    re = [] 
    for a in soup.findAll('div', attrs = {'id' : 'reviews'}):
        print('hello3')
        for b in a.findAll('div', attrs = {'class' : '_1gw6tte'}):
            print('hello4')
            for c in b.findAll('div', attrs = {'class' : '_czm8crp'}):
                re.append(c.text)
    return(re)

def gethostname(soup):
    for a in soup.findAll('div', attrs = {'class' : '_kicpfv'}):
        for b in a.findAll('div', attrs = {'class' : '_8b6uza1'}):
            h_name = b.text
            return(h_name)
            
            
            
def gethostjoindate(soup):
    join = []
    for b in soup.findAll('div', attrs = {'id' : 'host-profile'}):
        print('hello5')
        for c in b.findAll('div', attrs = {'class' : '_10ejfg4u'}):
            for d in c.findAll('div', attrs = {'class' : '_czm8crp'}):
                join.append(d.text)
    return(join)
    
def gethostnreviews(soup):
    host_re = []
    for b in soup.findAll('div', attrs = {'id' : 'host-profile'}):
        for e in b.findAll('div', attrs = {'class' : '_rqfxvmb'}):
            print('zzz = ' + str(e))
            host_re.append(e.text)
            print('eee =  ' + str(e.text))
        print('host = ' + str(host_re))
    if(len(host_re) > 2):
        return host_re[1]
    else:
        return host_re
    
def getverification(soup):
    veri = ''
    for b in soup.findAll('div', attrs = {'id' : 'host-profile'}):
        for k in b.findAll('div', attrs = {'class' : '_rqfxvmb'}):
            veri = k.text
    return(veri)
    
def getlangrrrt(soup):
    arr = []
    language = None
    rr = None
    rt = None
    for b in soup.findAll('div', attrs = {'id' : 'host-profile'}):
        for f in b.findAll('span', attrs = {'class' : '_czm8crp'}):
            print('hello6')
            print('text = ' + str(f.text))
            for g in f.findAll('span', attrs = {'class' : '_1p3joamp'}):
                if(f.text[0:10] == 'Languages:'):
                    print('in language')
                    language = g.text
                if(f.text[0:14] == 'Response rate:'):
                    print('in respo rate')
                    rr = g.text
                if(f.text[0:14] == 'Response time:'):
                    print('respo time')
                    rt = g.text
               
    arr.append(language)
    arr.append(rr)
    arr.append(rt)
    print('arr = ' + str(arr))
    if(len(arr) == 3):
        return(arr)
    else:
        return None
            
def gethostlink(soup):
    for a in soup.findAll('div', attrs = {'class' : '_1ij6gln6'}):
        link = a.find('a').get('href')
        return(link)
        
def gethostreviews(soup):
    host_reviewss = []
    for a in soup.findAll('div', attrs = {'class' : '_2h22gn'}):
        for b in a.findAll('section'):
            hostr = []
            for c in b.findAll('div', attrs = {'class' : '_czm8crp'}):
                text = c.text
                hostr.append(text)
            host_reviewss.append(hostr)

    new = (host_reviewss[(len(host_reviewss)-1)])
    return(new)


options = webdriver.FirefoxOptions()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
driver = webdriver.Firefox(options=options, executable_path="C:/Utility/BrowserDrivers/geckodriver.exe")
driver.get("https://www.airbnb.co.in/s/California--United-States/homes?source=mc_search_bar&click_referer=t%3ASEE_ALL%7Csid%3A24c6a9c7-fb90-419d-b482-ec3c6e21d7f6%7Cst%3ALANDING_PAGE_MARQUEE&refinement_paths%5B%5D=%2Fhomes&map_toggle=false&search_type=filter_change&place_id=ChIJPV4oX_65j4ARVW8IJ6IJUYs&checkin=2020-01-30&checkout=2020-01-31&adults=1&room_types%5B%5D=Shared%20room")
wait = WebDriverWait(driver, 7)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_1mslzuoh")))
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_ky9opu0")))
for i in range(0,8):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(4)
content = driver.page_source
time.sleep(3)
driver.close()
time.sleep(3)
soup = BeautifulSoup(content,'lxml')
time.sleep(2)
for a in soup.findAll('div', attrs={'class':'_1mslzuoh'}):
    links = 'https://www.airbnb.co.in' + str(a.find("a").get('href'))
    names = a.find("a").get('aria-label')
    if((a.find('span',attrs = {'class':'_ky9opu0'})) == None):
        rtr = None
    else:
        rtr = (a.find('span',attrs = {'class':'_ky9opu0'})).text
    link.append(links)
    name.append(names)
    ratings.append(rtr)
    
link = link[0:100]
name = name[0:100]
ratings = ratings[0:100]    
    
for i in range(0,100):
    print('link = ' + str(link[i]))
    soup = getsoup(link[i])
    amen = getamenities(soup)
    amenities.append(amen)
    nrev = getnreviews(soup)
    nofreviews.append(nrev)
    rev = getreviews(soup)
    reviews.append(rev)   
    hostna = gethostname(soup)
    hostname.append(hostna)
    joinda = gethostjoindate(soup)
    hostjoiningdate.append(joinda)
    hostnre = gethostnreviews(soup)
    host_nreviews.append(hostnre)
    verif = getverification(soup)
    verification.append(verif)
    langrrrt = getlangrrrt(soup)
    if(langrrrt == None):
        langrrrt = getlangrrrt(soup)
    else:
        host_languages.append(langrrrt[0])
        response_rate.append(langrrrt[1])
        response_time.append(langrrrt[2])
    hostlin = gethostlink(soup)
    if(hostlin == None):
        hostlin = gethostlink(soup)
    host_link.append('https://www.airbnb.co.in' + str(hostlin))
    
for i in range(0,len(host_link)):
    soup = getsssoup(host_link[i])
    host_rev = gethostreviews(soup)
    host_review.append(host_rev)
    
d = dict({'Name' : name, 'Link' : link, 'Rating' : ratings,'Amenities' : amenities, 'No of Review' : nofreviews, 'Reviews' : reviews,'Host-Name' : hostname, 'Host joining date' : hostjoiningdate, 'Response Rate' : response_rate, 'Response Time' : response_time ,'Host Languages':host_languages ,'Host no of reviews' : host_nreviews,'Verification' : verification, 'Host reviews' :host_review})
df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in d.items() ]))       
df.to_csv('california_sharedroom.csv', index=False, encoding='utf-8')
    
    

