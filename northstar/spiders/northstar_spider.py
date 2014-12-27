from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from northstar.items import NorthstarItem

class NorthstarSpider(CrawlSpider):
     name = 'northstar'
     allowed_domains = ['northstarteens.org']
     start_urls = ['http://northstarteens.org/blog/?currentPage=2']
     rules = (
         Rule(LinkExtractor(allow=['/blog/\?currentPage=\d+']), follow=True),
         Rule(LinkExtractor(allow=['/blog/[\w-]+\.html']), 'parse_blog'),
         )
     
     def parse_blog(self, response):
         items = []
         item = NorthstarItem()
         item['title'] = response.xpath("//a[@class='journal-entry-navigation-current']/text()").extract()
         tags = response.xpath("//span[@class='tag-element']/a/text()").extract()
         item['tags'] = ','.join(str(tag) for tag in tags if tag.strip())
         items.append(item)

         return items
