from setuptools import setup, find_packages
from setuptools.command.install import install
import os


setup(
    name='slackgup',
    version=open('VERSION').read().strip(),
    #version=__version__,
    author='Francesco De Carlo',
    author_email='decarlof@gmail.com',
    url='https://github.com/xray-imaging/slackgup',
    packages=find_packages(),
    include_package_data = True,
    scripts=['bin/slack'],
    description='cli to create slack channel as GUP-# and share it with the users listed in the GUP',
    zip_safe=False,
)