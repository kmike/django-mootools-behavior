========================
django-mootools-behavior
========================

Utilities for https://github.com/anutron/behavior integration with django.

This app provides template filters that can alter data attributes of the form
fields required for behavior. It also have a 'behavior' and 'behavior-more'
libraries bundled for use with django.contrib.staticfiles.

The license is MIT.

Installation
============

::

    pip install django-mootools-behavior

Configuration
=============

1. Add 'mootools_behavior' to INSTALLED_APPS;
2. (optional) run ``python manage.py collectstatic`` in order to get 'behavior'
   javascript files;
3. include the necessary js into html and use provided template filters
   in order to set attributes for form elements.

Filters
=======

behave
------

Sets 'data-behavior-...' attribute to a form field::

    {% load mootools_behavior %}

    <!-- data-behavior:"OverText" will be added to input field -->
    {{ form.title|behave:"OverText" }}


set_data
--------

Sets HTML5 data attribute ( http://ejohn.org/blog/html-5-data-attributes/ ).

Example::

    {% load mootools_behavior %}

    <!-- data-behavior:"OverText" will be added to input field -->
    {{ form.title|set_data:"behavior:OverText" }}

Contributing
============

If you've found a bug, implemented a feature or have a suggestion,
do not hesitate to contact me, fire an issue or send a pull request.

Source code:

* https://bitbucket.org/kmike/django-mootools-behavior/
* https://github.com/kmike/django-mootools-behavior/

Report bugs:

* https://bitbucket.org/kmike/django-mootools-behavior/issues
* https://github.com/kmike/django-mootools-behavior/issues
