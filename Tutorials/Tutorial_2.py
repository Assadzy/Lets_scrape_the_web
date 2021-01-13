import requests
from lxml import html

page = requests.get('https://www.firstround.com/companies/')

content = html.fromstring(page.content)

main_container = content.xpath('//div[@class="panel-group"]')

containers = main_container[0].xpath('.//div[@class="panel-heading"]')

for container in containers:
    title = container.xpath('.//b/text()')

    print('__ title is : ', title)

    detail = container.xpath('.//span[@class="hide-mobile"]/text()')

    print('__ detail is : ', detail)

    location = container.xpath('.//p[@class="company-location"]/text()')

    print('__ location is : ', location)

    link = container.xpath('.//a[@class="status-link"]/@href')
    print('__ link is : ', link)
