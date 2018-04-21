from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


def get_requirements(file_name):
    req_path = path.join(here + '/requirements', file_name)
    with open(req_path, encoding='utf-8') as f:
        return f.read().splitlines()


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pypeline',

    version='0.0.0',

    description='A framework to build pipeline in Python',
    long_description=long_description,

    url='https://github.com/humu1us/pypeline',

    author='Felipe Ortiz, Pablo Ahumada',
    author_email='fortizc@gmail.com, pablo.ahumadadiaz@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='pipeline',
    packages=find_packages(exclude=['contrib', 'docs', 'test']),
    install_requires=get_requirements('default.txt'),
    setup_requires=get_requirements('test.txt'),
    test_suite='test',
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={}
)
