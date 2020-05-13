# (C) 2020 University of Colorado AES-CCAR-SEDA (Space Environment Data Analysis) Group
# Written by Liam M. Kilcommons - University of Colorado, Boulder - 
# Colorado Center for Astrodynamics Research
# May, 2020
import os
import glob

os.environ['DISTUTILS_DEBUG'] = "1"

from setuptools import setup
from setuptools.command import install as _install

setup(name='nasaomnireader',
      version = "0.1.0",
      description = "Tools for using heliophysics parameters from NASA OMNIWeb",
      author = "Liam Kilcommons",
      author_email = 'liam.kilcommons@colorado.edu',
      url = "https://github.com/lkilcommons/nasaomnireader",
      download_url = "https://github.com/lkilcommons/nasaomnireader",
      long_description = ("Dict-like interface to NASA Common Data Format"
                         +" files from NASA OMNIWeb. HTTPS and requests"
                         +" used to access the data"),
      install_requires=['numpy','matplotlib','scipy','requests'],
      packages=['nasaomnireader'],
      package_dir={'nasaomnireader' : 'nasaomnireader'},
      license='LICENSE.txt',
      zip_safe = False,
      classifiers = [
            "Development Status :: 4 - Beta",
            "Topic :: Scientific/Engineering",
            "Intended Audience :: Science/Research",
            "License :: MIT",
            "Natural Language :: English",
            "Programming Language :: Python"
            ]
      )
