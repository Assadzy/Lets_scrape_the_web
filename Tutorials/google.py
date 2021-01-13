from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/search?client=safari&rls=en&q=donald+trump&ie=UTF-8&oe=UTF-8')
f = open('google.csv', 'w')
f.write('Title,Link,Detail')
for element in driver.find_elements_by_xpath('//div[@class="rc"]'):
    title = element.find_element_by_xpath('.//h3').text
    link = element.find_element_by_xpath('.//div[@class="yuRUbf"]/a').get_attribute('href')
    detail = element.find_element_by_xpath('.//span[@class="aCOpRe"]').text
    f.write(title.replace(',','|')+','+link.replace(',','|')+','+detail.replace(',','|')+'\n')


f.close()
