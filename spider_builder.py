# Import scrapy and CrawlerProcess 
import scrapy
from scrapy.crawler import CrawlerProcess

# Create the Spider ckass
class Your_Spider(scrapy.Spider):
    name = "your_spider"
    # start_requests method
    def start_requests(self):
        urls = ['https://www.datacamp.com/courses/all']
        for url in urls:
            yield scrapy.Request(url  = url,
                             callback = self.parse_1)
    # First parsing method
    def parse_1(self, response):
        # locate and extract a list of links from the original url webpage 
        course_blocks = response.css('div.course-block')
        course_links = course_blocks.xpath('./a/@href')
        links_to_follow = course_links.extract()
        for url in links_to_follow:
            yield response.follow(url = url,
                                  callback = self.parse_2)
    # Second parsing method            
    def parse_2(self, response):
        crs_title = response.xpath('//h1[contains(@class,"title")]/text()')
        crs_title_ext = crs_title.extract_first().strip()
        ch_titles = response.css('h4.chapter__title::text')
        ch_titles_ext = [t.strip() for t in ch_titles.extract()]
        dc_dict[ crs_title_ext ] = ch_titles_ext
    
# Initate an empaty dictionary to store the info scraped from the web for 
# later analysis
dc_dict=dict()
# Initiate a crawler process
process = CrawlerProcess()
# Tell the process which spider to use
process.crawl(Your_Spider)
# Start the crawling process
process.start()

print(dc_dict)
