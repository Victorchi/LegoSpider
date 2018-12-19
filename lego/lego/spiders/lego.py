import datetime
import re

from scrapy.spiders import CrawlSpider
from scrapy_redis.spiders import RedisCrawlSpider
from lego.items import LegoItem
from lego.dbutils import get_doc_of_response, get_md5


class LegoSpider(CrawlSpider):
    name = 'legospider'
    custom_settings = {
        'ITEM_PIPELINES': {
            'lego.pipelines.LegoPipeline': 300,
        },

    }

    vendor = 'lego'
    tablename_insert = 'lego'
    start_urls = ['https://shop.lego.com/en-US/category/sales-and-deals',
                  'https://shop.lego.com/en-DE/category/sales-and-deals',
                  'https://shop.lego.com/en-AU/category/sales-and-deals',
                  'https://shop.lego.com/en-BE/category/sales-and-deals',
                  'https://shop.lego.com/en-CA/category/sales-and-deals',
                  'https://shop.lego.com/en-CZ/category/sales-and-deals',
                  'https://shop.lego.com/en-DK/category/sales-and-deals',
                  'https://shop.lego.com/en-FI/category/sales-and-deals',
                  'https://shop.lego.com/en-FR/category/sales-and-deals',
                  'https://shop.lego.com/en-IT/category/sales-and-deals',
                  'https://shop.lego.com/en-NL/category/sales-and-deals',
                  'https://shop.lego.com/en-NZ/category/sales-and-deals',
                  'https://shop.lego.com/en-PT/category/sales-and-deals',
                  'https://shop.lego.com/ko-KR/category/sales-and-deals',
                  'https://shop.lego.com/en-CH/category/sales-and-deals',
                  'https://shop.lego.com/en-GB/category/sales-and-deals',
                  'https://shop.lego.com/en-AT/category/sales-and-deals'
                  ]
    collection = 'lego'

    def parse(self, response):
        item = LegoItem()
        try:
            pages = int(re.sub('.+of | re.+', '', response.xpath(
                '//div[@class="Summary__TextWrapper-s1u2s14y-1 fxTHUY"]/span[@class="Text__BaseTag-aa2o0i-0-span cTCaBe"]/text()').extract()[
                0])) // 18 + 1
        except:
            pages = 1

        for page in range(1, pages + 1):
            # 翻页
            page_link = response.url + '?page={page}'.format(page=str(page))
            doc = get_doc_of_response(page_link)
            contents = doc.xpath('//a[@data-test="product-leaf-title-link"]')
            for content in contents:
                try:
                    product_link = response.urljoin(content.xpath('@href')[0])
                    product_title = content.xpath('h2/span/text()')[0]
                    product_img = content.xpath('../../../../div/div/a/img/@src')[0]
                    product_price = \
                    content.xpath('../div[@data-test="product-leaf-price"]/div/span[@color="orange_dark"]/text()')[0]
                    product_id = content.xpath('../span/text()')[0]
                    product_slaes_month = ''
                    product_slaes_count = ''
                    product_stock = ''
                except Exception as e:
                    print(e)
                    continue
                item['shop_avatar'] = ''
                item['shop_name'] = "lego"
                item['product_link'] = product_link
                item['product_title'] = product_title
                item['product_img'] = product_img
                item['product_price'] = product_price
                item['product_slaes_month'] = product_slaes_month
                item['product_slaes_count'] = product_slaes_count
                item['product_stock'] = product_stock
                item['product_id'] = product_id
                item['_id'] = get_md5(product_link)
                item['collection'] = self.collection

                yield item
