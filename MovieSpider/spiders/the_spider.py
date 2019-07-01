import scrapy
from ..items import MoviespiderItem


class TheMovieSpider(scrapy.Spider):
    name = 'greatspider'

    start_urls = [
        'https://www.imdb.com/chart/top'
    ]

    def parse(self, response):
        items = MoviespiderItem()

        the_table = response.css('.titleColumn')

        for tab in the_table:
            title = tab.css('.titleColumn a::text').extract()
            year = tab.css('.secondaryInfo::text').extract()

            items['title'] = title
            items['year'] = year

            yield items