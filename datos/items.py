# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DatosItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = scrapy.Field()
    descripcion = scrapy.Field()
    actualizado = scrapy.Field()
    filas = scrapy.Field()
    columnas = scrapy.Field()
    propietario = scrapy.Field()
