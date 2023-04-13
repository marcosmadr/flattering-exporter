from spider_exporter.spiders import FlatteringExporterBaseSpider


class TestSpider1(FlatteringExporterBaseSpider):
    name = "example_1.1"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    item_schema = {
        'url': 'someurl',
        'text': 'some text',
        'author': [{
            'link': '/author/Albert-Einstein',
            'name': 'Albert Einstein'
        }],
        'tags': [
            {'tag': 'test', 'link': 'http://www.somelink.com'},
            {'tag': 'test2', 'link': 'http://www.somelink.com'},
            {'tag': 'test3', 'link': 'http://www.somelink.com'},
            {'tag': 'test4', 'link': 'http://www.somelink.com'},
        ],
    }
    options = {}
    renaming = [
        (r"^author\[0\]->", ""),
    ]

    flattering_kwargs = {'field_options': options, 'headers_renaming': renaming}

    def parse(self, response):
        for q in response.css('.quote'):
            item = {
                'url': response.url,
                'text': q.css('.text::text').get(),
                'author': [{
                    'name': q.css('.author::text').get(),
                    'link': q.xpath('.//a/@href').get(),
                }],
                'tags': [
                    {'tag': _q.css('::text').get(), 'link': _q.css('::attr(href)').get()}
                    for _q in q.css('.tag')
                ],
            }
            yield item
