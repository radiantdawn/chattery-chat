import os
from setuptools import setup, find_packages

install_requires = []


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()

args = dict(
    name='chattery',
    version='0.1.0',
    description=('Chattery chat'),
    long_description=read('README.rst'),
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'],
    author='...',
    author_email='...',
    url='https://github.com/radiantdawn/chattery-chat',
    packages=find_packages(exclude=('tests')),
    install_requires=install_requires)
setup(**args)
