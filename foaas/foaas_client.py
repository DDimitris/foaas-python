import random
import json
from .foaas_response import FuckingResponse

__AUTHOR__ = 'Dimitris Dedousis <dimitris.dedousis@gmail.com>'
__LICENSE__ = 'MIT'
__VERSION__ = '1.0.0'


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

    def __init__(self, url=GLOBAL_URL):
        self.initialized = False
        self.url = url

    def __getattr__(self, method_name):
        if not self.initialized:
            self.initialized = True
            self.foperations = FuckingOperations(self.url)
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
        final_url = self.url + url_split[1] + "/"
        for i in range(2, len(url_split)):
            final_url += kwargs[url_split[i].replace(":", "") + "_"] + "/"
        final_url = final_url[:-1]
        if all(keys in kwargs for keys in ('shoutcloud_', 'i18n_')):
            if kwargs['shoutcloud_'] == True:
                final_url += "?shoutcloud&i18n=" + kwargs['i18n_']
            else:
                final_url += "?i18n=" + kwargs['i18n_']
        elif 'shoutcloud_' in kwargs:
            final_url += "?shoutcloud" if kwargs['shoutcloud_'] == True else ""
        elif 'i18n_' in kwargs:
            final_url += "?i18n=" + kwargs['i18n_']
        return final_url

    def random(self, **kwargs):
        actions = []
        urls_list = self.foperations.list_of_urls()
        string_of_names = ""
        for key, value in kwargs.items():
            string_of_names += key
        for url in urls_list:
            url_split = url.replace(":", "").split('/')[2:]
            #TODO: Bug detected!! In case the user provide shoutcloud and i18n 
            #This if statement will fail thus an exception will raise because of
            #no available action.
            if len(kwargs.items()) == len(url_split):
                if all(x in string_of_names for x in url_split):
                    actions.append(url)
        return FuckingResponse(self.__build_url(random.choice(actions),
                                                **kwargs))

