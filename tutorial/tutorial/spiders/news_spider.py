import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"

    # allowed_domains = ["areadevelopment.com"]

    def start_requests(self):
        start_urls = [
            'https://www.areadevelopment.com/newsItems/' # Assuming this is a valid page containing the links
        ]
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        # Extract the URLs of the articles using CSS selectors
        articles = response.css('div#newsItems article a::attr(href)').getall()

        for article_url in articles:
            if article_url is not None:
                yield response.follow(article_url, self.parse_article)

    @staticmethod
    def parse_article(response):
        # Extract the content within the <section> tag using XPath
        content = response.xpath('//section[@class="areaArticleBody" and @itemprop="articleBody"]//text()').getall()
        content = ' '.join(content).strip()  # Combine and strip any excessive whitespace

        yield {
            'url': response.url,
            'content': content,
        }
