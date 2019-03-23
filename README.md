foaas-python
============

A simple Python library to [FOAAS].

[![build status](https://travis-ci.org/DDimitris/foaas-python.svg?branch=master)](https://travis-ci.org/DDimitris/foaas-python)
[![Coverage Status](https://coveralls.io/repos/github/DDimitris/foaas-python/badge.svg?branch=master)](https://coveralls.io/github/DDimitris/foaas-python?branch=master)


* **Author**: [Derek Payton]
* **Version**: 0.2.0
* **License**: [MIT]

Documentation
-------------

### Important Notes

1) The default URL used is: [https://foaas.com/](https://foaas.com)
2) Every argument used in every method that makes a request to the REST API, must be followed by an underscore (ex. name\_, from\_, company\_)

### Installation

This package relies on [requests] and should be installed with [pip]:

```
pip install foaas
```

### Basic Usage

Fuck off:

```
>>> import foaas
>>> fuck = foass.Fuck()
>>> print fuck.off(name_='Tom', from_='Chris').text
Fuck off, Tom. - Chris
```

Give me some fucking JSON:

```
>>> fuck.that(from_='Chris').json
{u'message': u'Fuck that.', u'subtitle': u'- Chris'}
```

Just get the fucking URL:

```
>>> print fuck.everything(from_='Chris').url
https://foaas.com/everything/Chris
```

Give me some random fucking things:

```
>>> print fuck.random(from_='Chris').text
Fuck you very much. - Chris
>>> print fuck.random(from_='Chris').text
Fuck my life. - Chris
>>> print fuck.random(name_='Tom', from_='Chris').text
Fuck me gently with a chainsaw, Tom. Do I look like Mother Teresa? - Chris
>>> print fuck.random(name_='Tom', from_='Chris').text
Fuck off, Tom. - Chris

```

Set a custom fucking URL:

```
>>> import foaas
>>> fuck = foaas.Fuck(url="https://foaas.herokuapp.com/")
>>> fuck.that(from_="Dimitris").url
u'https://foaas.herokuapp.com/that/Dimitris'

```

### Supported Actions

All the supported actions are described in the  [https://foaas.com/](https://foaas.com) website.
This package is able to be automatically up-to-date with every addition or removal of any action.
 

Testing
-------

```
$ python tests.py
...........
----------------------------------------------------------------------
Ran 11 tests in 12.729s

OK
```

... or use [tox]:

```
$ tox
```

[FOAAS]: http://foaas.com/
[Derek Payton]: http://dmpayton.com
[MIT]: https://github.com/dmpayton/foaas-python/blob/master/LICENSE
[requests]: http://python-requests.org/
[pip]: http://www.pip-installer.org/
[tox]: https://tox.readthedocs.org/
