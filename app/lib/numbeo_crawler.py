import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'numbeo crawler'
    start_urls = [
        'https://www.numbeo.com/cost-of-living/rankings_current.jsp',
        'https://www.numbeo.com/property-investment/rankings_current.jsp',
        'https://www.numbeo.com/crime/rankings_current.jsp',
        'https://www.numbeo.com/health-care/rankings_current.jsp',
        'https://www.numbeo.com/pollution/rankings_current.jsp',
        'https://www.numbeo.com/traffic/rankings_current.jsp',
        'https://www.numbeo.com/quality-of-life/rankings_current.jsp'
    ]

    def parse(self, response):
        headers = None
        for tr in response.css('thead tr'):
            headers = tr.css('th div::text').extract()
        results = []
        i = 1
        for tr in response.css('tbody tr'):
            city = tr.css('td.cityOrCountryInIndicesTable a::text').extract_first()
            values = tr.css('td::text').extract()
            values.insert(0, city)
            values.insert(0, i)
            i += 1
            results.append(dict(zip(headers, values)))
        print(results[:5])

