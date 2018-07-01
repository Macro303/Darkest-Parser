from setuptools import setup, find_packages

setup(
    name='Darkest Parser',
    version=1.1,
    description='Small little script to parse a .darkest file into a dictionary',
    author='Macro303',
    author_email='jackson.jonah@gmail.com',
    url='https://github.com/Macro303/Darkest-Parser',
    packages=find_packages(exclude=('test',)),
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
