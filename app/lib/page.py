import requests

from config import Configuration


class PageLoader:

    def __init__(self):
        self.config = Configuration()
        self.headers = {'User-Agent': self.config.user_agent}

    # получение html со страницы с пизжеными моцыками
    def get_page(self):
        return requests.get(self.config.bikepost_url, headers=self.headers)

    def get_page_by_url(self, url):
        return requests.get(url, headers=self.headers)
