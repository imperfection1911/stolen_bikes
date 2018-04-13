from app.page import PageLoader
from app.parser import Parser
from app.storage import Storage
import pprint


class StolenBikes:

    def __init__(self):
        self.storage = Storage()
        self.page = PageLoader()
        self.page_text = self.page.get_page().text
        # получаем ссылки на все моты на всех страницах
        bikes = []
        # первая страница
        bikes_page = self.get_bikes(self.page_text)
        for bike in bikes_page:
            bikes.append(bike)
        pages = self.get_pages()
        for page in pages:
            new_page = PageLoader()
            page_text = new_page.get_page_by_url(page).text
            bikes_page = self.get_bikes(page_text)
            for bike in bikes_page:
                bikes.append(bike)
        bike_infos = []
        for bike in bikes:
            new_page = PageLoader()
            page_text = new_page.get_page_by_url(bike).text
            bike_infos.append(self.get_bike_info(page_text))
        print(bike_infos)
        self.storage.insert_many(bike_infos)
        pprint(self.storage.find({'details': {'Номер рамы:': 'ZDMM400AA1B008796'}}))

    def get_pages(self):
        parser = Parser(self.page_text)
        return parser.get_pages()

    @staticmethod
    def get_bikes(page):
        parser = Parser(page)
        return parser.get_stolen_bikes()

    @staticmethod
    def get_bike_info(page):
        parser = Parser(page)
        return parser.parse_bike_page()

if __name__ == "__main__":
    sb = StolenBikes()
