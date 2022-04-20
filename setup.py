# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


long_description = open('README.txt').read()


setup(
    name='django-taggit-autosuggest',
    version='1.0.1',
    description='Autosuggestions for django-taggit',
    long_description=long_description,
    author='Vizvasrj',
    author_email='vizvasrj@gmail.com',
    url='https://bitbucket.org/vizvasrj/django-taggit-autosuggest',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    install_requires=[
        'django-taggit',
    ],
)
