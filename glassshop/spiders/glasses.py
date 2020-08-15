import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['http://www.glassesshop.com/bestsellers']

    def parse(self, response):
        glasses_rows = response.xpath("//div[@id='product-lists']/div")

        for glasses in glasses_rows:
            url = glasses.xpath(".//div[@class='product-img-outer']/a/@href").get()
            url_image = glasses.xpath(".//img[@class='lazy d-block w-100 product-img-default']/@src").get()
            name = glasses.xpath(".//div[@class='p-title']/a/text()").get()
            price = glasses.xpath("normalize-space(.//div[@class='p-price']//span/text())").get()

            yield {
                'url': url,
                'url_image': url_image,
                'name': name,
                'price': price
            }
