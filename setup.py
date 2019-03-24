import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='foaas',
    version='1.0.0',
    description='A wrapper for the foaas framework',
    license='MIT',
    url='https://github.com/DDimitris/foaas-python',
    author='Dimitris Dedousis',
    author_email='dimitris.dedousis@gmail.com',
    py_modules=['foaas'],
    install_requires=['requests'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
    ),
)
