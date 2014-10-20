#!/usr/bin/python
# -*- coding: UTF-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

from setuptools import setup, find_packages

setup(
        name = 'instapush',
        version = '0.1.1',
        keywords = ('instapush', 'tools'),
        description = 'a python wrapper for instapush',
        license = 'MIT License',

        url = 'https://github.com/adamwen829/instapush-py',
        author = 'Adam Wen',
        author_email = 'adamwen829@gmail.com',

        packages = find_packages(),
        include_package_data = True,
        platforms = 'any',
        install_requires = ['requests']
)
