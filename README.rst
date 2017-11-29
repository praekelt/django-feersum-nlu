Django Feersum NLU
==================
**A django feersum nlu wrapper with helper methods and reusable views.**

.. image:: https://travis-ci.com/praekelt/django-feersum-nlu.svg?token=5Nj35BzFWCYFF3qyVG5B&branch=develop
    :target: https://travis-ci.com/praekelt/django-feersum-nlu

.. image:: https://coveralls.io/repos/github/praekelt/django-feersum-nlu/badge.svg?branch=develop
    :target: https://coveralls.io/github/praekelt/django-feersum-nlu?branch=develop

.. contents:: Contents
    :depth: 5

Requirements
------------

#. pip install feersum_nlu

#. A feersum_nlu AUTH_TOKEN and MODEL,
please check https://github.com/praekelt/feersum-nlu-api-wrappers for information


Installation
------------

#. Install or add ``django-feersum-nlu`` to your Python path.

#. Add ``feersumnlu`` to your ``INSTALLED_APPS`` setting.

#. Add ``url(r'^feersumnlu/', include("feersumnlu.urls", namespace="feersumnlu"))`` to your ``url patterns`` (only required if you intend on using the detail view)

#. Add FEERSUMNLU settings to django app settings.

Usage
-----

``django-feersum-nlu`` a django feersum nlu wrapper with helper methods and reusable views.


Settings
~~~~~~~~

The following settings are required for this module:
::
    FEERSUMNLU = {
        "AUTH_TOKEN": "YOUR AUTH TOKEN",
        "HOST": "https://nlu.playground.feersum.io:443/nlu/v2",
        "MODEL": "YOUR MODEL"
    }


Licence
-------
Please see the License requirements in the LICENSE file of this repository.
