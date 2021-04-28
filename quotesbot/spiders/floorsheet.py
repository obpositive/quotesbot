import scrapy


class BootstrapTableSpider(scrapy.Spider):
    name = "floorsheet"

    # urls =[ "http://http://118.91.175.170/main/floorsheet",]

    def start_requests(self):
        urls = [
            # "http://nepalstock.com/main/floorsheet/index/1/?contract-no=&stock-symbol=&buyer=&seller=&_limit=20000"
            # "http://www.nepalstock.com.np/floorsheet?contract-no=&stock-symbol=&buyer=&seller=&_limit=20000"
            # "http://nepalstock.com/main/floorsheet/index/1/contract-no/asc/?contract-no=&stock-symbol=&buyer=&seller=&_limit=50000"
            # "http://nepalstock.com.np/main/floorsheet/index/1/?contract-no=&stock-symbol=&buyer=&seller=&_limit=30000"
            # "http://nepalstock.com.np/main/floorsheet/index/2/?contract-no=&stock-symbol=&buyer=&seller=&_limit=30000" ,
            # "http://nepalstock.com.np/main/floorsheet/index/3/?contract-no=&stock-symbol=&buyer=&seller=&_limit=10000",
            # "http://nepalstock.com.np/main/floorsheet/index/4/?contract-no=&stock-symbol=&buyer=&seller=&_limit=10000"
            # "http://nepalstock.com.np/main/floorsheet/index/5/?contract-no=&stock-symbol=&buyer=&seller=&_limit=10000",
            # "http://nepalstock.com.np/main/floorsheet/index/1/?contract-no=&stock-symbol=&buyer=&seller=&_limit=20000",
            "http://nepalstock.com/main/floorsheet/index/1/?contract-no=&stock-symbol=&buyer=&seller=&_limit=30000",
            "http://nepalstock.com/main/floorsheet/index/4/?contract-no=&stock-symbol=&buyer=&seller=&_limit=10000",
            "http://nepalstock.com/main/floorsheet/index/5/?contract-no=&stock-symbol=&buyer=&seller=&_limit=10000",
            #"http://nepalstock.com/main/floorsheet/index/6/?contract-no=&stock-symbol=&buyer=&seller=&_limit=10000",
           # "http://nepalstock.com/main/floorsheet/index/7/?contract-no=&stock-symbol=&buyer=&seller=&_limit=10000",
           # "http://nepalstock.com/main/floorsheet/index/8/?contract-no=&stock-symbol=&buyer=&seller=&_limit=10000",
           # "http://nepalstock.com/main/floorsheet/index/9/?contract-no=&stock-symbol=&buyer=&seller=&_limit=10000",
            #"http://nepalstock.com/main/floorsheet/index/10/?contract-no=&stock-symbol=&buyer=&seller=&_limit=10000",
            #"http://nepalstock.com/main/floorsheet/index/11/?contract-no=&stock-symbol=&buyer=&seller=&_limit=10000"

        ]
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
    # def parse(self, response):
    # page = response.url.split("/")[-2]
    # filename = 'floorsheet.html' % page
    # with open(filename, 'wb') as f:
    # f.write(response.body)
    # self.log('Saved file' % filename)

# $ scrapy crawl --nolog -o - -t json floorsheet_table
