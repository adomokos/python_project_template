# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Python',
    long_description=readme,
    author='Attila Domokos',
    author_email='*',
    url='https://github.com/adomokos/python-starter-project',
    license=license,
    packages=find_packages(exclude=('tests', 'spec', 'docs'))
    entry_points={
        'console_scripts': [
            'sample=sample.__main__:main'
        ],
    },
)

