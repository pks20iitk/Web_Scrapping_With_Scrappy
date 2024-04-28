from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    @property
    def start_requests(self):
        urls = ['https://www.areadevelopment.com/',
                'https://www.areadevelopment.com/newsItems/4-26-2024/topsoe-chesterfield-county-virginia.shtml',
                'https://www.areadevelopment.com/newsItems/4-26-2024/kikkoman-foods-walworth-jefferson-wisconsin.shtml',
                'https://www.areadevelopment.com/newsItems/4-26-2024/bwx-technologies-cambridge-ontario.shtml',
                'https://www.areadevelopment.com/newsItems/4-26-2024/greenheck-group-knoxville-tennessee.shtml',
                'https://www.areadevelopment.com/newsItems/4-26-2024/local-bounti-corporation-pasco-washington.shtml',
                'https://www.areadevelopment.com/newsItems/4-26-2024/innovative-construction-group-siler-city-north-carolina.shtml',
                'https://www.areadevelopment.com/newsItems/4-25-2024/crystal-window-and-door-systems-mansfield-texas.shtml',
                'https://www.areadevelopment.com/newsItems/4-25-2024/jdsat-fairfax-county-virginia.shtml',
                'https://www.areadevelopment.com/newsItems/4-25-2024/trussworks-mid-america-jackson-missouri.shtml',
                'https://www.areadevelopment.com/newsItems/4-25-2024/epic-flight-academy-hebron-kentucky.shtml',
                'https://www.areadevelopment.com/newsItems/4-25-2024/epc-columbia-lebanon-kentucky.shtml',
                'https://www.areadevelopment.com/newsItems/4-22-2024/daisy-brand-boone-iowa.shtml',
                'https://www.areadevelopment.com/newsItems/4-22-2024/canfor-fulton-alabama.shtml',
                'https://www.areadevelopment.com/newsItems/4-19-2024/tucker-door-trim-henrico-county-virginia.shtml',
                'https://www.areadevelopment.com/newsItems/4-19-2024/zekelman-industries-blytheville-arkansas.shtml',
                'https://www.areadevelopment.com/newsItems/4-19-2024/fibrebond-corporation-webster-parish-louisiana.shtml',
                'https://www.areadevelopment.com/newsItems/4-19-2024/master-steel-hardeeville-south-carolina.shtml',
                'https://www.areadevelopment.com/newsItems/4-18-2024/l3harris-technologies-orange-county-virginia.shtml',
                'https://www.areadevelopment.com/newsItems/4-18-2024/republic-airways-holdings-tuskegee-alabama.shtml',
                'https://www.areadevelopment.com/newsItems/4-18-2024/south-africa-based-radel-winston-salem-north-carolina.shtml',
                'https://www.areadevelopment.com/newsItems/4-18-2024/firestone-industrial-products-dyersburg-tennessee.shtml',
                'https://www.areadevelopment.com/newsItems/4-18-2024/samsung-electronics-taylor-texas.shtml',
                'https://www.areadevelopment.com/newsItems/4-18-2024/omco-solar-huntsville-alabama.shtml',
                'https://www.areadevelopment.com/newsItems/4-18-2024/martco-allen-parish-louisiana.shtml',
                'https://www.areadevelopment.com/newsItems/4-18-2024/estes-energetics-bossier-parish-louisiana.shtml',
                'https://www.areadevelopment.com/newsItems/4-18-2024/benteler-steel-tube-manufacturing-port-of-caddo-bossier-louisiana.shtml',
                'https://www.areadevelopment.com/newsItems/4-18-2024/washington-penn-plastic-winchester-kentucky.shtml',
                'https://www.areadevelopment.com/newsItems/4-16-2024/epl-america-danville-virginia.shtml',
                'https://www.areadevelopment.com/newsItems/4-16-2024/certus-medical-ingham-county-michigan.shtml',
                'https://www.areadevelopment.com/newsItems/4-16-2024/kalmbach-feeds-wyandot-county-ohio.shtml',
                'https://www.areadevelopment.com/newsItems/4-15-2024/tesa-tape-grand-rapids-michigan.shtml',
                'https://www.areadevelopment.com/newsItems/4-15-2024/fujifilm-diosynth-biotechnologies-holly-springs-north-carolina.shtml',
                'https://www.areadevelopment.com/newsItems/4-15-2024/two-rivers-lumber-coosa-county-alabama.shtml',
                'https://www.areadevelopment.com/newsItems/4-15-2024/protomet-corporation-rockwood-tennessee.shtml',
                'https://www.areadevelopment.com/newsItems/4-14-2024/corkys-food-manufacturing-memphis-tennessee.shtml',
                'https://www.areadevelopment.com/newsItems/4-11-2024/spectrum-advanced-manufacturing-technologies-colorado-springs-colorado.shtml',
                'https://www.areadevelopment.com/newsItems/4-11-2024/norplas-industries-rossford-ohio.shtml',
                'https://www.areadevelopment.com/newsItems/4-11-2024/toagosei-america-west-jefferson-ohio.shtml',
                'https://www.areadevelopment.com/newsItems/4-11-2024/gracious-living-ky-morgantown-kentucky.shtml',
                'https://www.areadevelopment.com/newsItems/4-9-2024/vienna-beef-newcomerstown-ohio.shtml']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        self.log(f"got response from {response.url}")
        item = {
            "text": response.css(".areaArticleBody::text").getall()
        }

        yield item
