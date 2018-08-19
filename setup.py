#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import setuptools

here = Path(__file__).absolute().parent

README = here.joinpath('README.rst').read_text()
version = here.joinpath('VERSION').read_text().strip()

setuptools.setup(
    name='geometry3',
    version=version,
    author="Erik O'Shaughnessy",
    author_email='erik.oshaughnessy@gmail.com',
    description='Python geometry library',
    long_description=README,
    long_description_content_type='text/x-rst',
    classifiers=[
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License'
    ],
    keywords='geometry',
    url='https://github.com/jnyjny/geometry3',
    license='Apache License, Version 2.0',
    package_dir={ '':'src' },
    packages=setuptools.find_packages(where='src'),
)
