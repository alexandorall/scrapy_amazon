import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AmazonCrawlSpider(CrawlSpider):
    name = 'amazon_crawl'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=gaming+chairs&pd_rd_r=03a2570b-fa30-4f50-9b29-8d93f6fd06db&pd_rd_w=V7dcK&pd_rd_wg=qTw2k&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=TWNM8RRC7JWX5Z7KHCEM&ref=pd_gw_unk']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
