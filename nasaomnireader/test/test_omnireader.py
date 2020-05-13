# (C) 2020 University of Colorado AES-CCAR-SEDA (Space Environment Data Analysis) Group
# Written by Liam M. Kilcommons
from nasaomnireader import omnireader
import pytest
import numpy as np
from numpy import testing as nptest
import datetime,os,pkgutil

@pytest.fixture(params=['hourly','5min','1min'],
    ids=['hourly','5min','1min'])
def example_omni_interval(request):
    """
    A fixture that can have tests written around it,
    and each test will be executed for each parameter,
    that is, for each possible cadence
    """
    cadence = request.param
    dt = datetime.datetime(2006,3,14)
    return omnireader.omni_interval(dt,dt+datetime.timedelta(days=1),cadence)

def test_omnireader_can_download_txt():
    """
    Test that we can get to the omni FTP location
    for text files and that
    we have a sane local directory for storing files
    """
    dt = datetime.datetime(2005,1,1)
    od = omnireader.omni_downloader(cdf_or_txt='txt',force_download=True)
    fakecdf = od.get_cdf(dt,'5min')
    downloaded_txt = os.path.join(od.localdir,od.filename_gen['5min'](dt))
    assert os.path.exists(downloaded_txt)

@pytest.mark.skipif(pkgutil.find_loader('spacepy') is None,
                    reason="requires spacepy.pycdf, CDF reading library")
@pytest.fixture(params=['hourly','5min','1min'],
        ids=['hourly','5min','1min'])
def omni_interval_txtcdf_comparison(request):
    """
    A fixture that can have tests write around it,
    and each test will be executed for each parameter,
    that is, for each possible cadence
    """
    cadence = request.param
    dt = datetime.datetime(2006,3,14)
    omni_interval_args = (dt,dt+datetime.timedelta(days=1),cadence)
    oiformats = {
                'cdf':omnireader.omni_interval(*omni_interval_args,
                                                    cdf_or_txt='cdf',
                                                    force_download=True),

                'txt':omnireader.omni_interval(*omni_interval_args,
                                                    cdf_or_txt='txt',
                                                    force_download=True)
                }
    return oiformats

# @pytest.mark.skipif(pkgutil.find_loader('spacepy') is None,
#                     reason="requires spacepy.pycdf, CDF reading library")
# def test_omnireader_can_download_cdf():
#     """
#     Test that we can get to the omni FTP and that
#     we have a sane local directory for storing files
#     """
#     dt = datetime.datetime(2005,1,1)
#     od = omnireader.omni_downloader(cdf_or_txt='cdf',force_download=True)
#     cdf = od.get_cdf(dt,'5min')
#     downloaded_cdf = os.path.join(od.localdir,os.path.split(od.filename_gen['5min'](dt))[-1])
#     assert os.path.exists(downloaded_cdf)

# @pytest.mark.skipif(pkgutil.find_loader('spacepy') is None,
#                     reason="requires spacepy.pycdf, CDF reading library")
# def test_omniinterval_txt_cdf_same_epoch(omni_interval_txtcdf_comparison):
#     """
#     Compare the first epoch value of the day and make sure it's the same
#     """
#     oi_txt = omni_interval_txtcdf_comparison['txt']
#     oi_cdf = omni_interval_txtcdf_comparison['cdf']
#     eptxt,epcdf = oi_txt['Epoch'][0],oi_txt['Epoch'][0]
#     assert eptxt == epcdf

if __name__ == '__main__':
    pytest.main()
