import scrapy
import re
from scrapy.loader import ItemLoader
from real_estate_parser.items import FrankSaltItem, strip_processor


class FrankSaltSpider(scrapy.Spider):
    name = 'franksalt'
    recursion_depth = 4

    def __init__(self, url=None, *args, **kwargs):
        print(url)
        super(FrankSaltSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url] if url else ['https://franksalt.com.mt/advanced-search/?status=forSale&propertyType%5B%5D=3&bedrooms=&referenceNum=&currency=eur']
        for url in self.start_urls:
            regex = r'(?<=[&?]paged=)\d+'
            pattern = re.search(regex, url)
            if pattern:
                re.sub(regex, '1', url)
            else:
                url += '&paged=1'

    def parse(self, response):
        items = response.css('div.property-grid-item')
        if len(items) == 0:
            return

        for item in items:
            item_url = item.css('a.property-read-more').attrib.get('href')
            yield scrapy.Request(item_url, self.parse_item)

        page = int(re.search(r'(?<=[?&]paged=)\d+', response.url).group(0))
        if page >= self.recursion_depth > 0:
            return
        next_url = re.sub(r'(?<=[?&]paged=)\d+', str(page + 1), response.url)
        yield response.follow(next_url, self.parse)

    @staticmethod
    def parse_item(response):
        features = {
            strip_processor(feature.css('p.media-heading::text').get()):
                feature.css('p.media-heading>b::text').get()
            for feature in response.css('div.rooms-features-box div.feature-container')
        }

        l = ItemLoader(FrankSaltItem(), response=response)
        l.add_css('name', 'h1.property-ref::text')
        l.add_css('ref_id', 'h1.property-ref strong::text')
        l.add_css('price', 'h2.property-price>span::text')
        l.add_css('locality', 'p.property-location::text')

        l.add_value('bedrooms', features.get('No of Bedrooms:'))
        l.add_value('finish', features.get('Finish:'))
        l.add_value('garden', features.get('Garden (dims):', features.get('Surrounding Garden:')))
        l.add_value('views', features.get('Has Views:', features.get('Type of View:')))
        l.add_value('pool', features.get('Swimming Pool:'))
        l.add_value('url', response.url)
        return l.load_item()
