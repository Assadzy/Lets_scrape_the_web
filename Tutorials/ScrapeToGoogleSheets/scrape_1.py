import requests
from lxml import html
from urllib.parse import urljoin
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np

def parse(content):
    list = []
    containers = content.xpath('//div[@class="quote"]')
    for container in containers:
        quote = container.xpath('.//span[@class="text"]/text()')
        auther = container.xpath('.//small[@class="author"]/text()')
        tag1 = container.xpath('.//div[@class="tags"]/a[1]/text()')
        tag2 = container.xpath('.//div[@class="tags"]/a[2]/text()')
        tag3 = container.xpath('.//div[@class="tags"]/a[3]/text()')
        output.append([quote, auther, tag1, tag2, tag3])
        #print([quote, auther, tag1, tag2, tag3])
    next_page = content.xpath('//li[@class="next"]/a/@href')
    return next_page, list
def request(url):
    page = requests.get(url)
    content = html.fromstring(page.content)
    next_page, list = parse(content)

    if next_page != []:
        next_page = urljoin('https://quotes.toscrape.com/', next_page[0])
        request(next_page)

def auth():
    scope = ['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('google_auth_key.json', scope)
    gs = gspread.authorize(credentials)
    sh = gs.open('quote')
    return sh

output = []
bb = request('https://quotes.toscrape.com/')
worksheet = auth().worksheet('Sheet1')
output = [[str(x[0]) for x in element if x!=[]] for element in output]
array = np.array(output)

# Write the array to worksheet starting from the A2 cell
worksheet.update('A2', array.tolist())
