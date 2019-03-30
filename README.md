foaas-python
============

A simple Python library to [FOAAS].

[![build status](https://travis-ci.org/DDimitris/foaas-python.svg?branch=master)](https://travis-ci.org/DDimitris/foaas-python)
[![Coverage Status](https://coveralls.io/repos/github/DDimitris/foaas-python/badge.svg?branch=master)](https://coveralls.io/github/DDimitris/foaas-python?branch=master)


* **Author**: [Dimitris Dedousis]
* **Version**: 1.0.0
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
>>> from foaas.foaas_client import Fuck
>>> fuck = Fuck()
>>> print fuck.off(name_='Tom', from_='Chris').text
Fuck off, Tom. - Chris
```

Print in JSON format:

```
>>> fuck.that(from_='Chris').json
{u'message': u'Fuck that.', u'subtitle': u'- Chris'}
```

Print the URL:

```
>>> print fuck.everything(from_='Chris').url
https://foaas.com/everything/Chris
```

Print random responses:

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

Set a custom URL:

```
>>> from foaas.foaas_client import Fuck
>>> fuck = Fuck(url="https://foaas.herokuapp.com/")
>>> fuck.that(from_="Dimitris").url
u'https://foaas.herokuapp.com/that/Dimitris'

```
Internationalization and localization support:

```
>>> from foaas.foaas_client import Fuck
>>> fuck = Fuck()
>>> print(fuck.that(from_="Dimitris", i18n_="es").text)
Joder que !!,., !! - Dimitris undefined

```
Shoutcloud support:

```
>>> from foaas.foaas_client import Fuck
>>> fuck = Fuck()
>>> print(fuck.that(from_="Dimitris", shoutcloud_=True).text)
FUCK THAT. - DIMITRIS
```

### Supported Actions

All the supported actions are described in the  [https://foaas.com/](https://foaas.com) website.
This package is able to be automatically up-to-date with every addition or removal of any action.
 

Testing
-------

```
$ python tests.py
...............
----------------------------------------------------------------------
Ran 15 tests in 17.537s

OK
```

... or use [tox]:

```
$ tox
```

[FOAAS]: http://foaas.com/
[Dimitris Dedousis]: https://ddedousis.eu
[MIT]: https://github.com/DDimitris/foaas-python/blob/master/LICENSE 
[requests]: http://python-requests.org/
[pip]: http://www.pip-installer.org/
[tox]: https://tox.readthedocs.org/
