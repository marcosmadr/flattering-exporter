from spider_exporter.spiders import FlatteringExporterBaseSpider


class TestSpider2(FlatteringExporterBaseSpider):
    name = "example_2.1"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    item_schema = {
        'text': 'some text',
        'author': [
            {'name': 'name', 'value': 'Albert Einstein'},
            {'name': 'link', 'value': '/author/Albert-Einstein'},
        ],
        'tags': [
            'test',
        ],
    }
    options = {
        "tags": {
            "named": False, "grouped": True
        },
        "author": {
            "named": True, "name": "name", "grouped": True
        }
    }
    renaming = []

    flattering_kwargs = {'field_options': options, 'headers_renaming': renaming}

    def parse(self, response):
        for q in response.css('.quote'):
            item = {
                'text': q.css('.text::text').get(),
                'author': [
                    {'name': 'name', 'value': q.css('.author::text').get()},
                    {'name': 'link', 'value': q.xpath('.//a/@href').get()},
                ],
                'tags': [
                    _q.css('::text').get()
                    for _q in q.css('.tag')
                ],
            }
            yield item
