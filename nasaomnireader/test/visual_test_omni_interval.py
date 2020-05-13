# (C) 2020 University of Colorado AES-CCAR-SEDA (Space Environment Data Analysis) Group
# Written by Liam M. Kilcommons
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from nasaomnireader.omnireader import omni_interval
import datetime

_cadences = ['hourly','5min','1min']
_data_formats = ['cdf','txt']

class OmniIntervalParams(object):
    def __init__(self,varname,cadence,data_format):
        self.varname = varname
        self.cadence = cadence
        self.data_format = data_format

    @property
    def color(self):
        if self.cadence == 'hourly':
            return 'red'
        elif self.cadence == '5min':
            return 'green'
        elif self.cadence == '1min':
            return 'blue'
        else:
            raise ValueError('Invalid cadence {}'.format(self.cadence))

    @property
    def linestyle(self):
        if self.data_format is 'cdf':
            return '-'
        elif self.data_format is 'txt':
            return '--'

    def __str__(self):
        return '({})({})'.format(self.cadence,
                                self.data_format)



if __name__ == '__main__':

    f = plt.figure(figsize=(12,8))
    ax1 = f.add_subplot(511)
    ax2 = f.add_subplot(512)
    ax3 = f.add_subplot(513)
    ax4 = f.add_subplot(514)
    ax5 = f.add_subplot(515)
    axs = [ax1,ax2,ax3,ax4,ax5]

    centerdt = datetime.datetime(2007,11,19,18,10,15)
    ddt = datetime.timedelta(hours=4)
    startdt = centerdt-ddt
    enddt = centerdt+ddt

    for cadence in _cadences:
        for data_format in _data_formats:
            vsw_varname = 'flow_speed' if cadence != 'hourly' else 'V'
            dst_varname = 'SYM_H' if cadence != 'hourly' else 'DST'
            dens_varname = 'proton_density' if cadence != 'hourly' else 'N'
            params = []
            params.append(OmniIntervalParams('BY_GSM',cadence,data_format))
            params.append(OmniIntervalParams('BZ_GSM',cadence,data_format))
            params.append(OmniIntervalParams(vsw_varname,cadence,data_format))
            params.append(OmniIntervalParams(dst_varname,cadence,data_format))
            params.append(OmniIntervalParams(dens_varname,cadence,data_format))
            oi = omni_interval(startdt,enddt,cadence,cdf_or_txt=data_format)
            for param,ax in zip(params,axs):
                print('----{}{}----'.format(param.varname,param))
                ax.plot(oi['Epoch'],oi[param.varname],'k.',
                                    color=param.color,
                                    linestyle=param.linestyle,
                                    label=str(param))
                ax.set_ylabel(param.varname)

    ax1.legend(ncol=3,framealpha=.5)

    f.autofmt_xdate()
    f.savefig('omni_interval_test.png',dpi=300)


