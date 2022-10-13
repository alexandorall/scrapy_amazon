import scrapy
# 1 page amazon reviewes
 
class AmazonReviewsSpider(scrapy.Spider):
    name = 'amazon_reviews'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/Razer-DeathAdder-Essential-Gaming-Mouse/dp/B094PS5RZQ/ref=sr_1_1?keywords=gaming+mouse&pd_rd_r=aa367b1c-f357-4bb6-8cd2-51917fd2b694&pd_rd_w=mdg6Z&pd_rd_wg=AtxQb&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=XXWY93ZMZG9SYCDS2YNH&qid=1657525024&sr=8-1']

    def parse(self, response):
        #for div_list in response.xpath('//div[contains(@class, "review")]'):
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
                    