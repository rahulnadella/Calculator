"""
Calculator
----------

A simple implementation of a calculator containing several operators

Usage::

     import calculator
     
     calculator.add(10, 3) -> 13
     calculator.subtract(10, 3) -> 7
     calculator.multiply(10, 3) -> 30
     calculator.divide(10, 3) -> 3.3333333
     calculator.modulus(10, 3) -> 1
     calculator.squared(2) -> 4
     calculator.cubed(2) -> 8
     calculator.power(2, 5) -> 32
     calculator.sqrt(4) -> 2
     calculator.root(32, 5) -> 2
     calculator.abs(-2) -> 2

Other Links
```````````

* `development version
  <http://github.com/rahulnadella/calculator>`
"""
from setuptools import setup

setup(
    name='Calculator',
    version='1.0.0',
    url='http://github.com/rahulnadella/calculator',
    license='MIT',
    author='Rahul Nadella',
    author_email='rahulnadella@yahoo.com',
    description='A simple implementation of calculator',
    long_description=__doc__,
    py_modules=['calculator'],
    zip_safe=False,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
