from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from lxml import etree
from Book.items import BookItem


class Book(CrawlSpider):
    name = "bookSpider"
    start_urls = [
        "https://www.booktxt.net/4_4516/1639104.html"
    ]
    link = LinkExtractor(restrict_xpaths="//div[@class='bottem1']/a[contains(text(),'下一')]",attrs="href")
    rules = [
        Rule(link_extractor=link, callback="parse_item",follow=True)
    ]

    def parse_start_url(self, response):
        selector = etree.HTML(response.body)
        book = BookItem()
        titletext = selector.xpath("//h1/text()")[0].strip()
        if titletext.__contains__('章：'):
            title = titletext.split("章：")
        elif titletext.__contains__('章;'):
            title = titletext.split("章;")
        else:
            title = titletext
        if len(title) > 1:
            if len(title) > 1:
                text = selector.xpath("//div[@id='content']/text()")
                book["content"] = text
                book["title"] = title[1]
                return book
        else:
            print("-----------------------", title)

    def parse_item(self, response):
        selector = etree.HTML(response.body)
        book = BookItem()
        titletext = selector.xpath("//h1/text()")[0].strip()
        if titletext.__contains__('章：'):
            title = titletext.split("章：")
        elif titletext.__contains__('章;'):
            title = titletext.split("章;")
        else:
            title = ['',titletext]
        if len(title) > 1:
            if len(title) > 1:
                text = selector.xpath("//div[@id='content']/text()")
                book["content"] = text
                book["title"] = title[1]
                return book
        else:
            print("-----------------------", title)
