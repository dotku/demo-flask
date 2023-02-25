import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# specify the url
urlpage = 'https://groceries.asda.com/search/yogurt'
print(urlpage)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(10)
results = driver.find_elements(
    By.XPATH, "//*[@class=' co-product-list__main-cntr']//*[@class=' co-item ']//*[@class='co-product']//*[@class='co-item__title-container']//*[@class='co-product__title']")
print('Number of results', len(results))
print(results)

data = []
for result in results:
    product_name = result.text
    link = result.find_element(By.TAG_NAME, 'a')
    product_link = link.get_attribute("href")
    # append dict to array
    data.append({"product": product_name, "link": product_link})

# close driver
driver.quit()
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)
df.to_csv('asdaYogurtLink.csv')
