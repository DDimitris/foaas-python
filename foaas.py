import random
import requests
import json

__AUTHOR__ = 'Derek Payton <derek.payton@gmail.com>'
__LICENSE__ = 'MIT'
__VERSION__ = '0.2.0'


class FuckingResponse(object):

    def __init__(self, url):
        self.url = url
        self._html = None
        self._json = None
        self._text = None

    def make_request(self, accept):
        return requests.get(self.url, headers={
            'Accept': accept,
            'Accept-Language': 'en-us'
        })

    @property
    def text(self):
        if self._text is None:
            self._text = self.make_request('text/plain')
        return self._text.text

    @property
    def json(self):
        if self._json is None:
            self._json = self.make_request('application/json')
        return self._json.json()

    @property
    def html(self):
        if self._html is None:
            self._html = self.make_request('text/html')
        return self._html.text


class FuckingOperations(object):

    def __init__(self, url):
        self.operations_dict = json.loads(
            FuckingResponse(url + "operations").text)

    def list_of_urls(self):
        urls = list(map(lambda url_value: url_value['url'],
                        self.operations_dict))
        return urls

    def list_of_actions(self):
        actions = list(map(lambda url: url.split('/')[1], self.list_of_urls()))
        return actions

    def dict_of_actions_urls(self):
        actions_dict = dict(map(lambda item: (item['url'].split(
            '/')[1], item['url']), self.operations_dict))
        return actions_dict


class Fuck(object):

    GLOBAL_URL = "https://foaas.com/"

    def __init__(self):
        self.initialized = False

    def __getattr__(self, method_name):
        if not self.initialized:
            self.initialized = True
            self.foperations = FuckingOperations(self.GLOBAL_URL)
            for action, url in self.foperations.dict_of_actions_urls().items():
                self.__add_meta_method(action, url)
            return getattr(self, method_name)
        else:
            raise AttributeError(
                "The method you are trying to call does not exists!")

    def __add_meta_method(self, action, url):

        def method(self, **kwargs):
            final_url = self.__build_url(url, **kwargs)
            return FuckingResponse(final_url)

        setattr(Fuck, action, method)

    def __build_url(self, url, **kwargs):
        url_split = url.split('/')
        final_url = self.GLOBAL_URL + url_split[1] + "/"
        for i in range(2, len(url_split)):
            final_url += kwargs[url_split[i].replace(":", "") + "_"] + "/"
        return final_url[:-1]

    def random(self, **kwargs):
        actions = []
        urls_list = self.foperations.list_of_urls()
        string_of_names = ""
        for key, value in kwargs.items():
            string_of_names += key
        for url in urls_list:
            url_split = url.replace(":", "").split('/')[2:]
            if len(kwargs.items()) == len(url_split):
                if all(x in string_of_names for x in url_split):
                    actions.append(url)
        return FuckingResponse(self.__build_url(random.choice(actions),
                                                **kwargs))

    def setFuckingAddress(self, address):
        self.GLOBAL_URL = address

fuck = Fuck()
