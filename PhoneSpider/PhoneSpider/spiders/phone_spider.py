import scrapy
import logging


class PhoneSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
            'https://www.devicespecifications.com/en',
            ]

    def parse(self, response):
        brand_urls = response.xpath('//div[@class="brand-listing-container-frontpage"]/a/@href').extract()
        for brand_url in brand_urls:
            yield response.follow(brand_url, self.parse_brand)

    def parse_brand(self, response):
        device_urls = response.xpath('//div[@class="model-listing-container-80"]/div/a/@href').extract()
        for device_url in device_urls:
            yield response.follow(device_url, self.parse_device)

    def parse_device(self, response):
        device_brand = response.xpath('//td[text()="Brand"]/../td[2]/text()').extract()
        device_model = response.xpath('//td[text()="Model"]/../td[2]/text()').extract()
        device_alias = response.xpath('//td[text()="Model alias"]/../td[2]/text()').extract()
        yield {
                'brand': device_brand,
                'model': device_model,
                'alias': device_alias,
                'url': response.url,
                }
