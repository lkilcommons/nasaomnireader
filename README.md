# nasaomnireader
Tools for reading NASA OMNIWeb data

The tools in this packaged used to be part of lkilcommons/geospacepy-lite. As of version 0.2 of geospacepy-lite, nasaomnireader is now it's own package.

If you need fast OMNI data reading I recommend installing:

1. [The NASA CDF Library](http://cdf.gsfc.nasa.gov/)

2. [Spacepy](https://pypi.python.org/pypi/SpacePy), for it's pyCDF python interface to the NASA CDF Library

If geospacepy-lite does not detect SpacePy on your computer, it will use the NASA OMNIWeb ASCII text files.


### Installation Instructions ###

* Clone the repository
* `python setup.py install`

Example code using omnireader:
```{python}
from geospacepy import omnireader
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
