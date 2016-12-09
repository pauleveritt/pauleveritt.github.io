#!/usr/bin/env python

import codecs
from setuptools import setup

# Version info -- read without importing
_locals = {}
with open('sphinxstrap4/_version.py') as fp:
    exec(fp.read(), None, _locals)
version = _locals['__version__']

# README into long description
with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='sphinxstrap4',
    entry_points={
        'sphinx_themes': [
            'path = sphinxstrap4:get_path',
        ]
    },
    version=version,
    description='Sphinx theme based on Bootstrap 4',
    long_description=readme,
    author='Paul Everitt',
    author_email='pauleveritt@me.com',
    url='https://github.com/pauleveritt/sphinxstrap4',
    packages=['sphinxstrap4'],
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
