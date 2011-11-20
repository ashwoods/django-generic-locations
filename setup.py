#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = open('VERSION').read().lstrip('version: ').rstrip('\n')

#TODO: make this pypi compatible
setup(name='django-generic-locations',
      version = VERSION,
      packages=find_packages(),
      exclude_package_data={'rh2': ['bin/*.pyc']},
      setup_requires = ["setuptools_git >= 0.3",],
      requires = ['django-countries','django']

)
