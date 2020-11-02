# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

if __name__ == '__main__':
    setup(
        name='lcs',
        version=open('version.txt', 'r').read(),
        description='Longest Common Substring in python3.',
        author='Darius Russell Kish',
        packages=find_packages(),
        install_requires=[],
        setup_requires=["pytest-runner"],
        tests_require=["pytest"],
        include_package_data=True,
        zip_safe=False,
        scripts=[]
    )
