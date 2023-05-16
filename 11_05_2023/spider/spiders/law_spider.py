import scrapy

class LawSpider(scrapy.Spider):
    name = 'law'
    start_urls = ['https://pravo.by/document/?guid=3871&p0=H10200090']

    def parse(self, response, **kwargs):
        for article in response.css('.article'):
            print(article)
            yield {
                'article': article.css('::text').get()
            }

