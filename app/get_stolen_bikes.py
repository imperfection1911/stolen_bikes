import time
from config import Configuration
from lib.page import PageLoader
from lib.parser import Parser
from lib.storage import Storage


class StolenBikes:

    def __init__(self):
        while True:
            self.config = Configuration()
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
            # чистим хранилище перед инсертом
            self.storage.clear()
            self.storage.insert_many(bike_infos)
            time.sleep(int(self.config.interval))

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
