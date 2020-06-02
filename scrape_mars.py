#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import requests
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd


# # NASA Mars News

# In[2]:


url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


# In[3]:


response = requests.get(url)


# In[4]:


soup = BeautifulSoup(response.text, 'html.parser')


# In[5]:


#Find the title
news_title = soup.title.text
print(news_title)


# In[6]:


#Find the first paragraph
news_p = soup.find_all('p')
for paragraph in news_p:
    print(paragraph.text)


# # JPL Mars Space Images - Featured Image

# In[7]:


#Get splinter
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[8]:


#Have splinter expand image
full_image_button = browser.find_by_id("full_image")
full_image_button.click()


# In[9]:


#More info
browser.is_element_present_by_text("more info", wait_time=1)
more_info_element = browser.find_link_by_partial_text("more info")
more_info_element.click()


# In[10]:


# Parse Results HTML with BeautifulSoup
html = browser.html
image_soup = BeautifulSoup(html, "html.parser")


# In[11]:


img_url = image_soup.select_one("figure.lede a img").get("src")
img_url


# In[12]:


featured_image_url = f"https://www.jpl.nasa.gov{img_url}"
print(featured_image_url)


# # Mars Facts

# In[13]:



executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://space-facts.com/mars/'
browser.visit(url)


# In[14]:


#scrape the table containing facts about the planet
tables = pd.read_html(url)
tables


# In[15]:


#create dataframe
df = tables[0]
df.columns = ['0','1']
df.head()


# In[16]:


#set index
df.set_index('0', inplace=True)
df.head()


# In[17]:


html_table = df.to_html()
html_table


# In[18]:


html_table.replace('\n', '')


# In[19]:


df.to_html('table.html')


# # Mars Hemispheres

# In[39]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[40]:


hemisphere_image_urls = []

# list all the hemispheres
links = browser.find_by_css("a.product-item h3")
for item in range(len(links)):
    hemisphere = {}
    
    # click the links
    browser.find_by_css("a.product-item h3")[item].click()
    
    # find hemiphere titles
    hemisphere["title"] = browser.find_by_css("h2.title").text
    
    # find image url
    sample_element = browser.find_link_by_text("Sample").first
    hemisphere["img_url"] = sample_element["href"]
    
    
    # Append the dictionary with the image url string and the hemisphere title to a list
    hemisphere_image_urls.append(hemisphere)
    browser.back()


# In[41]:


hemisphere_image_urls


# # Step 2 - MongoDB and Flask Application

# In[ ]:




