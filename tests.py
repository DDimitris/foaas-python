import unittest
from foaas import Fuck, FuckingResponse

GLOBAL_URL = "https://foaas.com/"

class FuckingTests(unittest.TestCase):
    def setUp(self):
        self.fuck = Fuck()

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
        fuckingResponse = FuckingResponse("http://www.example.comoperations")
        with self.assertRaises(Exception):
            fuckingResponse.make_request("text/plain")

if __name__ == '__main__':
    unittest.main()
