from spider_exporter.spiders import FlatteringExporterBaseSpider


class TestSpider2(FlatteringExporterBaseSpider):
    name = "example_2.2"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    item_schema = {
        'text': 'some text',
        'tags': [
            {'tag': 'test'},
        ],
    }
    options = {
        "tags": {
            "named": True, "name": "tag", "grouped": True
        }
    }
    renaming = []

    flattering_kwargs = {'field_options': options, 'headers_renaming': renaming}

    def parse(self, response):
        for q in response.css('.quote'):
            item = {
                'text': q.css('.text::text').get(),
                'tags': [
                    _q.css('::text').get() for _q in q.css('.tag')
                ],
            }
            yield item
