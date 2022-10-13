import scrapy
# all pages amazon reviews

class AmazonR2Spider(scrapy.Spider):
    name = 'amazon_r2'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=gaming+mouse&pd_rd_r=aa367b1c-f357-4bb6-8cd2-51917fd2b694&pd_rd_w=mdg6Z&pd_rd_wg=AtxQb&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=XXWY93ZMZG9SYCDS2YNH&ref=pd_gw_unk']

    def parse(self, response):

        nextpage_link = response.css('span.s-pagination-strip a.s-pagination-next::attr(href)')      
        
        for link in response.css('div.s-title-instructions-style a::attr(href)'):
            yield response.follow(link, callback=self.parse_div)
        #yield {'nextpage_link': nextpage_link}
        yield from response.follow_all(nextpage_link, callback=self.parse)

    def parse_div(self, response):

        for div_list in response.css('div.review'):

            if div_list.css('div.reviewText span::text'):
                
                if div_list.css('a.review-title-content span::text'):

                    yield{
                        'product_name': response.css('span.product-title-word-break::text').get().strip(),                
                        'title_reviews': div_list.css('a.review-title-content span::text').get(),                   
                        'reviews': div_list.css('div.reviewText span::text').getall() 
                    }
                else:
                    yield{
                        'product_name': response.css('span.product-title-word-break::text').get().strip(),  
                        'title_reviews': 'Top review from other countries',                                 
                        'reviews': div_list.css('div.reviewText span::text').getall() 
                    }