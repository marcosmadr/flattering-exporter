import io
from flattering import Exporter, StatsCollector
from scrapy.exporters import BaseItemExporter


class CsvFlatteringItemExporter(BaseItemExporter):

    def __init__(self, file, item_schema, flattering_kwargs=None, **kwargs):
        super().__init__(dont_fail=True, **kwargs)
        self.file = io.TextIOWrapper(
            file,
            line_buffering=False,
            write_through=True,
            encoding=self.encoding,
            newline="",
        )
        sc = StatsCollector()
        sc.process_items([item_schema])
        self.exporter = Exporter(
            sc.stats["stats"],
            sc.stats["invalid_properties"],
            **(flattering_kwargs if flattering_kwargs else {})
        )

    def start_exporting(self):
        self.exporter.export_csv_headers(self.file)

    def export_item(self, item):
        self.exporter.export_csv_row(item, self.file, append=True)
