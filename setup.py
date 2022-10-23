"""DataFrame to test fixture converter"""

import setuptools
from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

version = {}
with open("pytest_pandera/version.py") as fp:
    exec(fp.read(), version)

setup(
   name='df2fixture',
   version=version['__version__'],
   description='DataFrame to test fixture converter',
   license="MIT",
   long_description=long_description,
   long_description_content_type="text/markdown",
   author='Dmitry Vazhenin',
   author_email='dmitry.stw@gmail.com',
   url="https://github.com/pulsarcomet/df2fixture",
   download_url = '',
   packages=['df2fixture'],
   keywords = ['pandas', 'pytest', 'fixtures'],
   classifiers=[
       "Development Status :: 3 - Alpha",
       "Intended Audience :: Developers",
       "License :: OSI Approved :: MIT License",
       "Programming Language :: Python :: 3",
       "Programming Language :: Python :: 3.7",
       "Programming Language :: Python :: 3.8",
       "Programming Language :: Python :: 3.9",
       "Programming Language :: Python :: 3.10",
       "Operating System :: OS Independent"
   ],

   install_requires=[
       'pandas',
       'numpy',
       'pytest'
   ],

   python_requires='>=3.7'
)
