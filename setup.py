"""DataFrame to test fixture converter"""

import setuptools
from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='df2fixture',
   version='0.2',
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
       "License :: OSI Approved :: Apache Software License",
       "Operating System :: OS Independent",
   ],

   install_requires=[
       'pandas',
       'numpy'
   ],

   python_requires='>=3.6'
)
