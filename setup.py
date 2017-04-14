#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup

setup(
        name='daily-note',
        version='0.2',
        py_modules=['note'],
        install_requires=[
            'click', ],
        entry_points='''
        [console_scripts]
        note=note:daily_note
        ''')
