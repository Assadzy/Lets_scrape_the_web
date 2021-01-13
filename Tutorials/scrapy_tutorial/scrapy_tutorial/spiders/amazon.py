import scrapy

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/gp/most-wished-for/books/283155/ref=s9_acsd_ri_bw_clnk/ref=s9_acsd_ri_bw_c2_x_c2cl?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-12&pf_rd_r=XPFTS0S5F37QCAZ4KTPM&pf_rd_t=101&pf_rd_p=5ce6d8b8-5077-495c-9f75-aa09194de846&pf_rd_i=283155']

    def parse(self, response):
        containers = response.xpath('//li[@role="gridcell"]')
        for container in containers:
            name = container.xpath('.//a[@class="a-link-normal"]/div/text()').extract_first().strip()
            page = container.xpath('.//a[@class="a-link-normal"]/@href').extract_first().strip()
            auther = container.xpath('.//a[@class="a-size-small a-link-child"]/text()').extract_first()
            rating = container.xpath('.//a[@class="a-size-small a-link-normal"]/text()').extract_first()
            price = container.xpath('.//a[@class="a-link-normal a-text-normal"]//span[@class="p13n-sc-price"]/text()').extract_first()


            yield { 'Name' : name,
                    'Page Link' : page,
                    'Auther Name' : auther,
                    'Rating' : rating,
                    'Price' : price,
                    }
