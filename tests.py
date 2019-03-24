import unittest
from src.foaas import Fuck, FuckingOperations
from src.foaas_response import FuckingResponse

GLOBAL_URL = "https://foaas.com/"
WRONG_URL = "http://www.example.comoperations"


class FuckingTests(unittest.TestCase):

    def setUp(self):
        self.fuck = Fuck()
        self.fResponse = FuckingResponse(WRONG_URL)
        self.fOperations = FuckingOperations(GLOBAL_URL)

    def test_url(self):
        url = self.fuck.off(name_='Alice', from_='Bob').url
        self.assertEqual(GLOBAL_URL + "off/Alice/Bob", url)

    def test_url_quoting(self):
        url = self.fuck.donut(name_='Alice!', from_='Bobby McGee').url
        self.assertEqual(GLOBAL_URL + "donut/Alice!/Bobby McGee", url)

    def test_html(self):
        html = self.fuck.thanks(from_='Bob').html
        self.assertIn('<h1>Fuck you very much.</h1>', html)
        self.assertIn('<em>- Bob</em>', html)

    def test_json(self):
        json = self.fuck.life(from_='Bob').json
        self.assertEqual({
            'message': 'Fuck my life.',
            'subtitle': '- Bob'
        }, json)

    def test_text(self):
        text = self.fuck.thanks(from_='Bob').text
        self.assertEqual('Fuck you very much. - Bob', text)

    def test_random(self):
        self.fuck.random(from_='Chris')
        self.fuck.random(name_='Tom', from_='Chris')
        self.fuck.random(name_='Alice', from_='Bob', company_='Acme')
        self.fuck.random(name_='Alice', from_='Bob', reference_='Clara')

    def test_method_exists(self):
        with self.assertRaises(AttributeError):
            self.fuck.test_method(from_="Chris")

    def test_address(self):
        with self.assertRaises(Exception):
            self.fResponse.make_request("text/plain")

    def test_list_of_urls(self):
        lst = self.fOperations.list_of_urls()
        self.assertIsInstance(lst, list)
        self.assertTrue(lst)

    def test_list_of_actions(self):
        lst = self.fOperations.list_of_actions()
        self.assertIsInstance(lst, list)
        self.assertTrue(lst)

    def test_dict_of_actions_urls(self):
        dictionary = self.fOperations.dict_of_actions_urls()
        self.assertIsInstance(dictionary, dict)
        self.assertTrue(dictionary)

if __name__ == '__main__':
    unittest.main()
