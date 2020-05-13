# (C) 2020 University of Colorado AES-CCAR-SEDA (Space Environment Data Analysis) Group
# Written by Liam M. Kilcommons
import traceback
try:
    from nasaomnireader.omnireader_config import config
except:
    print(traceback.format_exc())
    from nasaomnireader.default_config import config
