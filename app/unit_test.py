import unittest
from lib.page import PageLoader
from lib.parser import Parser


class Test(unittest.TestCase):

    # проверка того что страница жива и мы можем до нее достучаться
    def test_get_page(self):
        page = PageLoader()
        response = page.get_page()
        self.assertEqual(response.status_code, 200)

    # проверка получения ссылок на пижженые моты
    def test_get_stolen_bikes(self):
        page = PageLoader()
        response = page.get_page()
        parser = Parser(response.text)
        links = parser.get_stolen_bikes()
        result = False
        if len(links) > 0:
            result = True
        self.assertTrue(result)

    # проверка получения
    def test_get_pages(self):
        page = PageLoader()
        response = page.get_page()
        parser = Parser(response.text)
        links = parser.get_pages()
        result = False
        if len(links) > 0:
            result = True
        self.assertTrue(result)

    def test_parse_bike_page(self):
        page = PageLoader()
        response = page.get_page().text
        parser = Parser(response)
        links = parser.get_stolen_bikes()
        response = page.get_page_by_url(links[0]).text
        parser = Parser(response)
        bike_info = parser.parse_bike_page()
        result = False
        if len(bike_info) > 0:
            result = True
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
