#!/usr/bin/env python
from setuptools import setup

version='0.1.1'

setup(
    name = 'django-mootools-behavior',
    version = version,
    author = 'Mikhail Korobov',
    author_email = 'kmike84@gmail.com',
    url = 'http://bitbucket.org/kmike/django-mootools-behavior/',
    download_url = 'http://bitbucket.org/kmike/django-mootools-behavior/get/tip.zip',
    description = 'Utilities for https://github.com/anutron/behavior integration with django.',
    long_description = open('README.rst').read(),
    license = 'MIT license',

    requires = ['django'],
    packages=['mootools_behavior', 'mootools_behavior.templatetags'],
    include_package_data = True,
    install_requires=['django-widget-tweaks >= 0.3'],
    zip_safe=False,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
