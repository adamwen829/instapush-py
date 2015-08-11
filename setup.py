#!/usr/bin/python
# -*- coding: UTF-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

import os
from setuptools import setup, find_packages


def get_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, 'instapush/version.py')) as f:
        locals = {}
        exec(f.read(), locals)
        return locals['VERSION']
    raise RuntimeError('No version info found.')

setup(
        name='instapush',
        version = get_version(),
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
