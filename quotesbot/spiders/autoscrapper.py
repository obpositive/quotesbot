import scrapy


class AutoScrapper(scrapy.Spider):
    name = "autoscrapper"

    # urls =[ "http://http://118.91.175.170/main/floorsheet",]
    index_count = 8
    urls = []

    def start_requests(self):
        i = 1
        while i <= index_count:
            urls.append("http://nepalstock.com/main/floorsheet/index/{index_count}/?contract-no=&stock-symbol=&buyer=&seller=&_limit=10000")
            i += 1
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for row in response.xpath('//*[@class="table my-table"]//tr'):
            yield {
                'S.N': row.xpath('td[1]//text()').extract_first(),
                'Contract No': row.xpath('td[2]//text()').extract_first(),
                'Stock Symbol': row.xpath('td[3]//text()').extract_first(),
                'Buyer Broker': row.xpath('td[4]//text()').extract_first(),
                'Seller Broker': row.xpath('td[5]//text()').extract_first(),
                'Quantity': row.xpath('td[6]//text()').extract_first(),
                'Rate': row.xpath('td[7]//text()').extract_first(),
                'Amount': row.xpath('td[8]//text()').extract_first(),
            }
