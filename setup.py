"""DataFrame to test fixture converter"""

import setuptools
from setuptools import setup

from df2fixture import __version__

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='df2fixture',
   version=__version__,
   description='DataFrame to test fixture converter',
   license="MIT",
   long_description=long_description,
   long_description_content_type="text/markdown",
   author='Dmitry Vazhenin',
   author_email='dmitry.stw@gmail.com',
   url="https://github.com/pulsarcomet/df2fixture",
   #download_url = '',
   packages=['df2fixture'],
   keywords = ['pandas', 'pytest', 'fixtures'],
   classifiers=[
       "Development Status :: 3 - Alpha",
       "Intended Audience :: Developers",
       "Programming Language :: Python :: 3",
       "License :: MIT",
       "Operating System :: OS Independent",
   ],

   install_requires=[
       'pandas',
       'numpy',
       'pytest'
   ],

   python_requires='>=3.7'
)
