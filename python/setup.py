from setuptools import setup, find_packages

setup(
    name='agensgraph-python',
    version='1.0.0',
    description='Psycopg2 type extension module for AgensGraph',
    install_requires=['psycopg2>=2.5.4'],

    packages=find_packages(exclude=['tests']),
    test_suite = "tests",

    author='Umar Hayat',
    author_email='skaisw@skaiworldwide.com',
    maintainer='Umar Hayat',
    maintainer_email='skaisw@skaiworldwide.com',
    url='https://github.com/skaiworldwide-oss/agensgraph-drivers',
    license='Apache License Version 2.0',
)
