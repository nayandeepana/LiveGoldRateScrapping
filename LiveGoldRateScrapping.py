from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep
path="G:/Python/Practice/chrome driver/chromedriver.exe"
s=Service(path)
driver=webdriver.Chrome(service = s)
while True:

    driver.get("https://vickygold.in/Liverate.html")
    sleep(2)
    searchstring=driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div/div[4]/div/div[2]/div[2]/div[2]/span/span")
    rate=searchstring.text
    print(rate)