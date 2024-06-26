import io
import re
from setuptools import setup, find_packages

with io.open('aiozk/__init__.py', encoding='utf-8') as f:
    version = re.search(r"__version__ = '(.+)'", f.read()).group(1)

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='aiozk',
    version=version,
    description='Asyncio client for Zookeeper.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Kirill Pinchuk',
    author_email='cybergrind@gmail.com',
    maintainer='Kirill Pinchuk',
    maintainer_email='cybergrind@gmail.com',
    url='http://github.com/micro-fan/aiozk',
    license='MIT',
    keywords=['zookeeper', 'asyncio', 'async'],
    packages=find_packages(
        exclude=[
            'tests', 'tests.*', 'docker', 'TAGS', '.projectile', '*.log',
        ],
    ),
    tests_require=[
        'coverage',
        'flake8',
        'pytest',
        'pytest-asyncio',
        'asynctest',
        'pytest-cov',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
    ],
)
