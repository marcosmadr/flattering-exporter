import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        for q in response.css('.quote'):
            item = {
                'text': q.css('.text::text').get(),
                'author': {
                    'name': q.css('.author::text').get(),
                    'link': q.xpath('.//a/@href').get(),
                },
                'tags': [
                    #_q.css('::text').get(): _q.css('::attr(href)').get()}
                    _q.css('::text').get()
                    for _q in q.css('.tag')
                ],
            }
            # breakpoint()
            yield item
