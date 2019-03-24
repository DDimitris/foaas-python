# The MIT License (MIT)
#
# Copyright (c) 2013 Derek Payton
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import requests

__AUTHOR__ = 'Derek Payton <derek.payton@gmail.com>'


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
