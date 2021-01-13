from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#driver.execute_script("return document.body.scrollHeight")

driver = webdriver.Chrome()
driver.get('https://fjlabs.com/portfolio/')
height = 0
while True:
    new_height = driver.execute_script("return document.body.scrollHeight")
    if height==new_height:
        break
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    sleep(3)
    height=new_height
containers = driver.find_elements_by_xpath('//div[@id="companies"]/div')[1:]
for container in containers:
    title = container.find_element_by_xpath('.//img').get_attribute('alt')
    website = container.find_element_by_xpath('.//a[@class="websiteUrl"]').get_attribute('href')
    year = container.find_element_by_xpath('.//span[@class="year"]').get_attribute('innerText')
    stage = container.find_element_by_xpath('.//span[@class="investment_stage"]').get_attribute('innerText')
    print(title, website, year, stage)
