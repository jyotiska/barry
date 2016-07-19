#!/usr/bin/env python

from setuptools import setup


setup(name='barry',
    version='0.1',
    description='All-rounder command line tool against spreadsheets',
    author='Jyotiska Khasnabish',
    author_email='jyotiska123@gmail.com',
    url='https://github.com/jyotiska/barry',
    packages=['barry'],
    entry_points = {
        'console_scripts': [
            'barry = barry:main',
        ],
    },
    install_requires=[
        'pandas==0.18.1'
    ],
    keywords='csv xls xlsx excel json convert spreadsheet'
)
