import unittest
from app.page import PageLoader
from app.parser import Parser

class Test(unittest.TestCase):

    # проверка того что страница жива и мы можем до нее достучаться
    def test_get_page(self):
        page = PageLoader()
        response = page.get_page()
        self.assertEqual(response.status_code, 200)

    def test_get_stolen_bikes(self):
        page = PageLoader()
        parser = Parser()
        response = page.get_page()
        links = parser.get_stolen_bikes(response.text)
        print(links)

    def test_get_pages(self):
        page = PageLoader()
        parser = Parser()
        response = page.get_page()
        links = parser.get_pages(response.text)
        print(links)



if __name__ == '__main__':
    unittest.main()
