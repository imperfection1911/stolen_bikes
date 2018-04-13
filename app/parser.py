from config import Configuration
from lxml import html


class Parser:

    def __init__(self, page):
        self.tree = html.fromstring(page)

    # получение ссылок на ворованые моты
    def get_stolen_bikes(self):
        stolen_bikes_list = self.tree.xpath('//ins[@class="moto-item"]')
        links = []
        for stolen_bike in stolen_bikes_list:
            link = stolen_bike.xpath('.//a/@href')[0]
            links.append(link)
        return links

    # получение ссылок на другие страницы
    def get_pages(self):
        pages_list = self.tree.xpath('//div[@class="pagination"]')[0]
        links = pages_list.xpath('.//a/@href')
        return links

    # парсинг страницы угнаной техники
    def parse_bike_page(self):
        info_body = self.tree.xpath('//div[@class="info_body"]')[0]
        title = info_body.xpath('.//h1[@class="title"]/text()')[0]
        image = info_body.xpath('.//img/@src')[0]
        description = info_body.xpath('.//div[@class="description"]/text()')
        description = description[0].replace('\r\n', '').strip()
        try:
            contact = info_body.xpath('.//li/text()')[0]
        except IndexError:
            contact = info_body.xpath('.//li/a/@href')[0]
        # получение основной инфы по угону
        info_rows = []
        info_label = info_body.xpath('.//dt/text()')
        info_data = info_body.xpath('.//dd/text()')
        for i in range(0, len(info_label)):
            try:
                info_rows.append([info_label[i], info_data[i]])
            except IndexError:
                reward = info_body.xpath('.//span[@class="stolen-reward"]/text()')[0]
                info_rows.append([info_label[i], reward])
        # превращаем инфу в словарь.
        info = {}
        for row in info_rows:
            info[row[0].replace('.', '')] = row[1]
        result = {'title': title,
                  'image': image,
                  'description': description,
                  'contact': contact,
                  'details': info}
        return result
