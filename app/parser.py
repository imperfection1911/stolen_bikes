from config import Configuration
from lxml import html


class Parser:

    def __init__(self):
        pass

    def get_stolen_bikes(self, page):
        tree = html.fromstring(page)
        stolen_bikes_list = tree.xpath('//ins[@class="moto-item"]')
        links = []
        for stolen_bike in stolen_bikes_list:
            link = stolen_bike.xpath('.//a/@href')[0]
            links.append(link)
        return links

    def get_pages(self, page):
        tree = html.fromstring(page)
        pages_list = tree.xpath('//div[@class="pagination"]')[0]
        links = pages_list.xpath('.//a/@href')
        return links
