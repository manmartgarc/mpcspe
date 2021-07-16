# -*- coding: utf-8 -*-
'''
Created on Thursday, 15th July 2021 2:55:19 pm
===============================================================================
@filename:  setup.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe material
@purpose:   setup tools for package
===============================================================================
'''
import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='mpcspe',
    version='0.0.1',
    author='Manuel Martinez',
    author_email='manmart@uchicago.edu',
    description='Past placement tests for the computer science waver',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pypa/sampleproject',
    project_urls={
        'Bug Tracker': 'https://github.com/pypa/sampleproject/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'mpcspe'},
    package_data={'mpcspe': ['testdata/*']},
    packages=setuptools.find_packages(where='mpcspe'),
    python_requires='>=3.6',
)
