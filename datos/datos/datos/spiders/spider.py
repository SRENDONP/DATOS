import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from datos.items import DatosItem


class DatosSpider(CrawlSpider):
	name = 'datos'
	item_count = 0
	allowed_domain = ['www.datos.gov.co']
	#start_urls = ['https://datos.gov.co/browse?limitTo=datasets&sortBy=newest&utf8']
	start_urls = ['https://datos.gov.co/browse?limitTo=datasets&sortBy=newest&utf8=&page=965']
	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//html/body/div[2]/div/div[5]/div/div[3]/div[3]/div[3]/div[1]/a[10]'))),
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//h2/a')),
							callback = 'parse_item', follow = False)
		}	
	
	
	def parse_item(self, response):
			mi_item = DatosItem

			mi_item['titulo'] = response.xpath('normalize-space(//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[1]/h1/span/span)').extract_first()
			mi_item['descripcion'] = response.xpath('normalize-space(//*[@id="app"]/div/div[2]/div/div/div[2]/div[1]/div/div/div)').extract_first()
			mi_item['actualizado'] = response.xpath('normalize-space(//*[@id="app"]/div/div[3]/div[1]/section/div[2]/dl/div[1]/div/div[1]/div/dd)').extract_first()
			mi_item['filas'] = response.xpath('normalize-space(//*[@id="app"]/div/div[3]/section[1]/div/div/dl/div[1]/dd)').extract_first()
			mi_item['columnas'] = response.xpath('normalize-space(//*[@id="app"]/div/div[3]/section[1]/div/div/dl/div[2]/dd)').extract_first()
			mi_item['propietario'] = response.xpath('normalize-space(//*[@id="app"]/div/div[3]/div[1]/section/div[2]/div/div[1]/table/tbody/tr[2]/td[2]/span)').extract_first()
			self.item_count += 1
			if self.item_count > 5:
				raise CloseSpider('item_exceeded')
			yield mi_item

print ("ejecutado")