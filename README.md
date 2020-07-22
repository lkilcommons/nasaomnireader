# nasaomnireader
Download, read, and manuipulate [NASA OMNIWeb](https://omniweb.gsfc.nasa.gov) data

[![Build Status](https://travis-ci.org/lkilcommons/nasaomnireader.svg?branch=master)](https://travis-ci.org/lkilcommons/nasaomnireader)

The tools in this packaged used to be part of lkilcommons/geospacepy-lite. As of version 0.2 of geospacepy-lite, nasaomnireader is now it's own package.

### Data Sources ###

The package automatically downloads data from the NASA OMNIWeb website. It can use data in two formats:

#### Text ####

By default, text files are downloaded and used. 

    WARNING: metadata for text files is supplied from dumped CDF file metadata. There is no way to verify that this metadata is valid for the text files.Contributor
  
#### CDF ####

The NASA CDF format files will be downloaded if the code finds the following packages on your computer:

1. [The NASA CDF Library](http://cdf.gsfc.nasa.gov/)

2. [Spacepy](https://pypi.python.org/pypi/SpacePy), for it's pyCDF python interface to the NASA CDF Library

### Installation Instructions ###

* Clone the repository
* `python setup.py install`

Example code using omnireader:
```{python}
from nasaomnireader import omnireader
#Create a time window
sTimeIMF = datetime.datetime(2010,1,1)
eTimeIMF = datetime.datetime(2010,1,3)

#omni_interval is a dictionary-like object 
#that you can use to get the omni data for
#any variable as a numpy array 
#for any span of time
omniInt = omnireader.omni_interval(sTimeIMF,eTimeIMF,'5min')
t = omniInt['Epoch'] #datetime timestamps
By,Bz = omniInt['BY_GSM'],omniInt['BZ_GSM']

```
### Who do I talk to? ###

* This repository was created and is managed by Liam M. Kilcommons at CU Boulder
