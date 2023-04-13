import scrapy


class FlatteringExporterBaseSpider(scrapy.Spider):

    @classmethod
    def update_settings(cls, settings):
        super().update_settings(settings)

        settings['FEED_EXPORTERS'] = {
            'csv': 'exporter.exporters.CsvFlatteringItemExporter'
        }
        settings['FEEDS'] = {
            'items-%(name)s-%(time)s.csv': {
                'item_export_kwargs': {
                    'item_schema': cls.item_schema,
                    'flattering_kwargs': cls.flattering_kwargs,
                },
                'format': 'csv',
            }
        }
