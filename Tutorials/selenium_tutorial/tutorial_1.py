from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.selenium.dev/documentation/en/')

title = driver.find_element_by_xpath('//h1[@id="the-selenium-browser-automation-project"]').text
print(title)
driver.close()
