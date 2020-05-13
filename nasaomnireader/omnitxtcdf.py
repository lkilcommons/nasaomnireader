# (C) 2020 University of Colorado AES-CCAR-SEDA (Space Environment Data Analysis) Group
# Written by Liam M. Kilcommons
metadata={
   "hourly":
   {
      "attrs":
      {
         "Discipline": "Space Physics>Interplanetary Studies",
         "TITLE": "Near-Earth Heliosphere Data (OMNI)",
         "TEXT": "Hourly averaged definitive multispacecraft interplanetary parameters data OMNI Data Documentation: http://omniweb.gsfc.nasa.gov/html/ow_data.html Additional data access options available at  SPDF's OMNIWeb Service: http://omniweb.gsfc.nasa.gov/ow.html COHOWeb-formatted OMNI_M merged magnetic field and plasma data http://cohoweb.gsfc.nasa.gov/ Recent OMNI 1-HR Updates News: http://omniweb.gsfc.nasa.gov/html/ow_news.html",
         "LINK_TEXT": "  Additional data access options available at    Recent 1-hr OMNI Updates",
         "alt_logical_source": "Combined_OMNI_1AU-MagneticField-Plasma-Particles_mrg1hr_1hour_cdf",
         "Instrument_type": "Plasma and Solar Wind Magnetic Fields (space) Particles (space) Electric Fields (space) Activity Indices",
         "MODS": "created August 2003; conversion to ISTP/IACG CDFs via SKTEditor Feb 2000 Time tags in CDAWeb version were modified in March 2005 to use the CDAWeb convention of having mid-average time tags rather than OMNI's original convention of start-of-average time tags.",
         "Source_name": "OMNI (1AU IP Data)>Merged 1 Hour Interplantary OMNI data",
         "ADID_ref": "NSSD0110",
         "Logical_file_id": "omni2_h0_mrg1hr_00000000_v01",
         "Acknowledgement": "NSSDC",
         "Generated_by": "King/Papatashvilli",
         "Project": "NSSDC",
         "Descriptor": "IMF, Plasma, Indices, Energetic Proton Flux",
         "Logical_source_description": "OMNI Combined, Definitive, Hourly IMF and Plasma Data, and Energetic Proton Fluxes, Time-Shifted to the Nose of the Earth's Bow Shock, plus Solar and Magnetic Indices",
         "PI_affiliation": "ADNET, NASA GSFC",
         "Generation_date": "Ongoing",
         "Rules_of_use": "Public",
         "LINK_TITLE": "OMNI Data documentation SPDF's OMNIWeb Service COHOWeb-formatted OMNI_M merged magnetic field and plasma data Release Notes",
         "HTTP_LINK": "http://omniweb.gsfc.nasa.gov/html/ow_data.html http://omniweb.gsfc.nasa.gov/ow.html http://cohoweb.gsfc.nasa.gov/ http://omniweb.gsfc.nasa.gov/html/ow_news.html",
         "Mission_group": "OMNI (Combined 1AU IP Data; Magnetic and Solar Indices) ACE Wind IMP (All) !___Interplanetary Data near 1 AU",
         "Data_type": "H0>Definitive Hourly",
         "Data_version": "1",
         "Time_resolution": "1 hour",
         "spase_DatasetResourceID": "spase://VMO/NumericalData/OMNI/PT1H",
         "PI_name": "J.H. King, N. Papatashvilli",
         "Logical_source": "omni2_h0_mrg1hr",
      },
      "vars":
      {
         "Ratio":
         {
            "column": 27,
            "attrs":
            {
               "FIELDNAM": "Alpha/prot. ratio",
               "SCALEMAX": 1.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.3",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU IP Alpha/proton ratio",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9.99900,
               "LABLAXIS": "1AU IP Alpha/Proton",
               "SCALEMIN": 0.00000,
            },
         },
         "AL_INDEX":
         {
            "column": 52,
            "attrs":
            {
               "FIELDNAM": "AL-index (1-h)",
               "SCALEMAX": 300.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "I6",
               "VALIDMIN": -5000.00000,
               "CATDESC": "AL - 1-hour AL-index, from WDC Kyoto (1963/001-1988/182)",
               "LABLAXIS": "1-h AL-index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 300.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": -5000.00000,
            },
         },
         "ABS_B":
         {
            "column": 8,
            "attrs":
            {
               "FIELDNAM": "Field Magnitude Avg.",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU IP Average B Field Magnitude, nT, (last currently-available OMNI B-field data Sep 07, 2015)",
               "LABLAXIS": "1AU IP Mag Avg B",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "PR-FLX_10":
         {
            "column": 45,
            "attrs":
            {
               "FIELDNAM": "PROT Flux >10 MEV",
               "SCALEMAX": 90000.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F8.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU Proton flux >10 MeV (1/(SQcm-ster-s))",
               "LABLAXIS": "1AU Protons>10 MeV",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 100000.00000,
               "UNITS": "1/(SQcm-ster-s)",
               "SCALETYP": "log",
               "SCALEMIN": 0.00000,
            },
         },
         "Mach_num":
         {
            "column": 37,
            "attrs":
            {
               "FIELDNAM": "Alfen mach number",
               "SCALEMAX": 500.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU IP Alfven mach number",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 500.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "LABLAXIS": "1AU IP Alfven Mach No.",
               "SCALEMIN": 0.00000,
            },
         },
         "AU_INDEX":
         {
            "column": 53,
            "attrs":
            {
               "FIELDNAM": "AU-index (1-h)",
               "SCALEMAX": 3000.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "I6",
               "VALIDMIN": -200.00000,
               "CATDESC": "AU - 1-hour AU-index,from WDC Kyoto (1963/001-1988/182)",
               "LABLAXIS": "AU-index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 3000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": -200.00000,
            },
         },
         "SIGMA-THETA-V":
         {
            "column": 33,
            "attrs":
            {
               "FIELDNAM": "sigma-theta-V",
               "SCALEMAX": 90.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": 0.00000,
               "CATDESC": "RMS deviation in plasma flow direction latitude (deg), theta",
               "LABLAXIS": "RMSDev Flow Lat",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "Deg",
               "SCALEMIN": 0.00000,
            },
         },
         "Rot#":
         {
            "column": 3,
            "attrs":
            {
               "FIELDNAM": "Bartels Rotation Number",
               "SCALEMAX": 9998.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "I4",
               "VALIDMIN": 1700.00000,
               "CATDESC": "Bartels Rotation Number",
               "LABLAXIS": "Bartel #",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 9998.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.00000,
               "UNITS": "  ",
               "SCALEMIN": 1700.00000,
            },
         },
         "PR-FLX_2":
         {
            "column": 43,
            "attrs":
            {
               "FIELDNAM": "PROT Flux > 2 MEV",
               "SCALEMAX": 90000.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F8.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU Proton flux >2 MeV (1/(SQcm-ster-s))",
               "LABLAXIS": "1AU Protons>2 MeV",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 100000.00000,
               "UNITS": "1/(SQcm-ster-s)",
               "SCALETYP": "log",
               "SCALEMIN": 0.00000,
            },
         },
         "PR-FLX_1":
         {
            "column": 42,
            "attrs":
            {
               "FIELDNAM": "PROT Flux > 1 MEV",
               "SCALEMAX": 900000.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "f9.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU Proton flux > 1 MeV ,1/(SQcm-ster-s), (last currently-available OMNI proton fluxes Sep 27, 2015",
               "LABLAXIS": "1AU Protons>1 MeV",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 900000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 1000000.00000,
               "UNITS": "1/(SQcm-ster-s)",
               "SCALETYP": "log",
               "SCALEMIN": 0.00000,
            },
         },
         "PR-FLX_4":
         {
            "column": 44,
            "attrs":
            {
               "FIELDNAM": "PROT Flux > 4 MEV",
               "SCALEMAX": 90000.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F8.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU Proton flux >4 MeV (1/(SQcm-ster-s))",
               "LABLAXIS": "1AU Protons>4 MeV",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "1/(SQcm-ster-s)",
               "SCALETYP": "log",
               "SCALEMIN": 0.00000,
            },
         },
         "Pressure":
         {
            "column": 28,
            "attrs":
            {
               "FIELDNAM": "Flow pressure",
               "SCALEMAX": 99.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU IP Flow pressure (nPa)",
               "LABLAXIS": "1AU IP Flow Pressure",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99.99000,
               "UNITS": "nPa",
               "SCALEMIN": 0.00000,
            },
         },
         "Beta":
         {
            "column": 36,
            "attrs":
            {
               "FIELDNAM": "Plasma beta",
               "SCALEMAX": 500.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F6.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU IP Plasma beta",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 500.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.98999,
               "LABLAXIS": "1AU IP Plasma Beta",
               "SCALEMIN": 0.00000,
            },
         },
         "PHI-V":
         {
            "column": 26,
            "attrs":
            {
               "FIELDNAM": "Flow longitude",
               "SCALEMAX": 90.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": -90.00000,
               "CATDESC": "1AU IP plasma flow direction longitude (deg), phi",
               "LABLAXIS": "1AU IP Flow Long",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "Deg",
               "SCALEMIN": -90.00000,
            },
         },
         "Day":
         {
            "column": 1,
            "attrs":
            {
               "FIELDNAM": "Decimal Day (JAN 1=1)",
               "SCALEMAX": 366.00000,
               "VAR_TYPE": "support_data",
               "FORMAT": "I3",
               "VALIDMIN": 1.00000,
               "CATDESC": "Decimal Day",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 366.00000,
               "FILLVAL": -2147483648.00000,
               "LABLAXIS": "Day",
               "SCALEMIN": 1.00000,
            },
         },
         "SIGMA-ABS_B":
         {
            "column": 17,
            "attrs":
            {
               "FIELDNAM": "sigma-ABS_B",
               "SCALEMAX": 50.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": 0.00000,
               "CATDESC": "RMS deviation of average B magnitude (nT)",
               "LABLAXIS": "RMSDev Mag Avg B",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 50.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "F":
         {
            "column": 10,
            "attrs":
            {
               "FIELDNAM": "Magnitude of avg. field vector",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU IP Magnitude of average field vector (nT)",
               "LABLAXIS": "1AU IP Mag Avg B-vector",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "PC_N_INDEX":
         {
            "column": 51,
            "attrs":
            {
               "FIELDNAM": "PC(N) index",
               "SCALEMAX": 25.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": -5.00000,
               "CATDESC": "PC - 1-hour Polar Cap index (North, Qaanaaq geomagnetic observatory), from DTU Space, Technical University of Denmark (Final 1975/001-2014/365)",
               "LABLAXIS": "1-h PC(N)-index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 25.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": " ",
               "SCALEMIN": -5.00000,
            },
         },
         "SIGMA-Bz":
         {
            "column": 21,
            "attrs":
            {
               "FIELDNAM": "sigma-Bz",
               "SCALEMAX": 110.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": 0.00000,
               "CATDESC": "RMS deviation Bz (nT), GSE",
               "LABLAXIS": "RMSDev Bz GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 110.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "N":
         {
            "column": 23,
            "attrs":
            {
               "FIELDNAM": "Ion density",
               "SCALEMAX": 150.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU IP Ion number density (per cc)",
               "LABLAXIS": "1AU IP N (ion)",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 150.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "Per cc",
               "SCALEMIN": 0.00000,
            },
         },
         "R":
         {
            "column": 39,
            "attrs":
            {
               "FIELDNAM": "Sunspot number v2 (daily)",
               "SCALEMAX": 400.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "I3",
               "VALIDMIN": 0.00000,
               "CATDESC": "Daily sunspot number V2, from  http://sidc.oma.be/silso/datafiles/ (1963/001-2015/243)",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 500.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.00000,
               "LABLAXIS": "Daily Sunspot No",
               "SCALEMIN": 0.00000,
            },
         },
         "PR-FLX_60":
         {
            "column": 47,
            "attrs":
            {
               "FIELDNAM": "PROT Flux >60 MEV",
               "SCALEMAX": 90000.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F8.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU Proton flux >60 MeV (1/(SQcm-ster-s))",
               "LABLAXIS": "1AU Protons>60 MeV",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 100000.00000,
               "UNITS": "1/(SQcm-ster-s)..",
               "SCALETYP": "log",
               "SCALEMIN": 0.00000,
            },
         },
         "V":
         {
            "column": 24,
            "attrs":
            {
               "FIELDNAM": "Flow speed",
               "SCALEMAX": 1200.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.0",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU IP plasma flow speed (km/s)",
               "LABLAXIS": "1AU IP Plasma Speed",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1200.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.00000,
               "UNITS": "Km/s",
               "SCALEMIN": 0.00000,
            },
         },
         "SIGMA-Bx":
         {
            "column": 19,
            "attrs":
            {
               "FIELDNAM": "sigma-Bx",
               "SCALEMAX": 50.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": 0.00000,
               "CATDESC": "RMS deviation Bx (nT), GSE",
               "LABLAXIS": "RMSDev Bx GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 50.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "SIGMA-By":
         {
            "column": 20,
            "attrs":
            {
               "FIELDNAM": "sigma-By",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": 0.00000,
               "CATDESC": "RMS deviation By (nT), GSE",
               "LABLAXIS": "RMSDev By GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "BX_GSE":
         {
            "column": 12,
            "attrs":
            {
               "FIELDNAM": "Bx, GSE",
               "SCALEMAX": 99.90000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": -99.90000,
               "CATDESC": "1AU IP Bx (nT), GSE",
               "LABLAXIS": "1AU IP Bx, GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.90000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "nT",
               "SCALEMIN": -99.90000,
            },
         },
         "PLS":
         {
            "column": 5,
            "attrs":
            {
               "FIELDNAM": "ID for SW Plasma spacecraft",
               "SCALEMAX": 98.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "I2",
               "VALIDMIN": 1.00000,
               "CATDESC": "OMNI ID code for the source spacecraft  for time-shifted IP plasma values (see OMNI documentation link for codes)",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 98.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99.00000,
               "LABLAXIS": "1AU IP Plasma S/C ID#",
               "SCALEMIN": 1.00000,
            },
         },
         "F10_INDEX":
         {
            "column": 50,
            "attrs":
            {
               "FIELDNAM": "F10.7 index (daily)",
               "SCALEMAX": 500.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": 30.00000,
               "CATDESC": "F10.7 - Daily 10.7 cm solar radio flux, units: 10**(-22) Joules/second/square-meter/Hertz, from NGDC (1963/001-2015/243)",
               "LABLAXIS": "Daily F10.7",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 500.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": " ",
               "SCALEMIN": 30.00000,
            },
         },
         "KP":
         {
            "column": 38,
            "attrs":
            {
               "FIELDNAM": "Kp*10 (3-h)",
               "SCALEMAX": 90.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "I2",
               "VALIDMIN": 0.00000,
               "CATDESC": "Kp - 3-hour Kp*10 (Kp=1-,1,1+ corresponds to 7,10,13), fromNGDC (1963/001-2015/243)",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99.00000,
               "LABLAXIS": "3-h Kp*10",
               "SCALEMIN": 0.00000,
            },
         },
         "BY_GSM":
         {
            "column": 15,
            "attrs":
            {
               "FIELDNAM": "By, GSM",
               "SCALEMAX": 99.90000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": -99.90000,
               "CATDESC": "1AU IP By (nT), GSM",
               "LABLAXIS": "1AU IP By, GSM",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.90000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "nT",
               "SCALEMIN": -99.90000,
            },
         },
         "HR":
         {
            "column": 2,
            "attrs":
            {
               "FIELDNAM": "Decimal Hour",
               "SCALEMAX": 23.00000,
               "VAR_TYPE": "support_data",
               "FORMAT": "I2",
               "VALIDMIN": 0.00000,
               "CATDESC": "Decimal Hour",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 23.00000,
               "FILLVAL": -2147483648.00000,
               "LABLAXIS": "Hour",
               "SCALEMIN": 0.00000,
            },
         },
         "MFLX":
         {
            "column": 49,
            "attrs":
            {
               "FIELDNAM": "M'SPH Flux Flag",
               "SCALEMAX": 6.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "I2",
               "VALIDMIN": -1.00000,
               "CATDESC": "Magnetospheric Contamination of 1AU Proton Flux code (6=No,<=5 see OMNI documentation)",
               "LABLAXIS": "M'Sph Contaminatn Flag",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 6.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 0.00000,
               "UNITS": "(6=No,1=All,-1=n/a)",
               "SCALEMIN": -1.00000,
            },
         },
         "Mgs_mach_num":
         {
            "column": 54,
            "attrs":
            {
               "FIELDNAM": "Magnetosonic mach number",
               "SCALEMAX": 30.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F4.1",
               "VALIDMIN": 0.00000,
               "VAR_NOTES": "Derived parameters are obtained from the following equations. Magnetosonic Mach number = V/Magnetosonic_speedMagnetosonic speed = [(sound speed)**2 + (Alfv speed)**2]**0.5The Alfven speed = 20. * B / N**0.5The sound speed = 0.12 * [T + 1.28*10**5]**0.5",
               "CATDESC": "1AU IP Magnetosonic mach number",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 30.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99.90000,
               "LABLAXIS": "1AU IP Magnetosonic  Mach No.",
               "SCALEMIN": 0.00000,
            },
         },
         "E":
         {
            "column": 35,
            "attrs":
            {
               "FIELDNAM": "Electric Field",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F6.2",
               "VALIDMIN": -50.00000,
               "CATDESC": "1AU IP Electric Field (mV/m)",
               "LABLAXIS": "1AU IP Electric Field",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.98999,
               "UNITS": "mV/m",
               "SCALEMIN": -50.00000,
            },
         },
         "AP_INDEX":
         {
            "column": 49,
            "attrs":
            {
               "FIELDNAM": "ap-index (3-h)",
               "SCALEMAX": 350.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "I3",
               "VALIDMIN": 0.00000,
               "CATDESC": "ap - 3-hour ap-index (1963/001-2015/243), from NGDC",
               "LABLAXIS": "3-h ap",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 350.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.00000,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "YR":
         {
            "column": 0,
            "attrs":
            {
               "FIELDNAM": "Year",
               "SCALEMAX": 2020.00000,
               "VAR_TYPE": "support_data",
               "FORMAT": "I4",
               "VALIDMIN": 1963.00000,
               "CATDESC": "Year",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 2020.00000,
               "FILLVAL": -2147483648.00000,
               "LABLAXIS": "Year",
               "SCALEMIN": 1963.00000,
            },
         },
         "PR-FLX_30":
         {
            "column": 46,
            "attrs":
            {
               "FIELDNAM": "PROT Flux >30 MEV",
               "SCALEMAX": 90000.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F8.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU Proton flux >30 MeV (1/(SQcm-ster-s))",
               "LABLAXIS": "1AU Protons>30 MeV",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 100000.00000,
               "UNITS": "1/(SQcm-ster-s)",
               "SCALETYP": "log",
               "SCALEMIN": 0.00000,
            },
         },
         "SIGMA-ratio":
         {
            "column": 34,
            "attrs":
            {
               "FIELDNAM": "sigma-ratio",
               "SCALEMAX": 1.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.3",
               "VALIDMIN": 0.00000,
               "CATDESC": "RMS deviation alpha/proton ratio",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9.99900,
               "LABLAXIS": "RMSDev A/P ratio",
               "SCALEMIN": 0.00000,
            },
         },
         "SIGMA-T":
         {
            "column": 29,
            "attrs":
            {
               "FIELDNAM": "sigma-T",
               "SCALEMAX": 9999980.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F8.0",
               "VALIDMIN": 0.00000,
               "CATDESC": "RMS deviation of plasma temperature (deg K)",
               "LABLAXIS": "RMSDev Temp",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 9999980.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999990.00000,
               "UNITS": "Deg K",
               "SCALEMIN": 0.00000,
            },
         },
         "SIGMA-V":
         {
            "column": 31,
            "attrs":
            {
               "FIELDNAM": "sigma-V",
               "SCALEMAX": 9998.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.0",
               "VALIDMIN": 0.00000,
               "CATDESC": "RMS deviation in plasma flow velocity (km/s)",
               "LABLAXIS": "RMSDev Speed",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 9998.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.00000,
               "UNITS": "Km/s",
               "SCALEMIN": 0.00000,
            },
         },
         "IMF":
         {
            "column": 4,
            "attrs":
            {
               "FIELDNAM": "ID for IMF spacecraft",
               "SCALEMAX": 98.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "I2",
               "VALIDMIN": 1.00000,
               "CATDESC": "OMNI ID code for the source spacecraft for time-shifted IMF values (see OMNI documentation link for codes)",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 98.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99.00000,
               "LABLAXIS": "1AU IMF S/C ID#",
               "SCALEMIN": 1.00000,
            },
         },
         "SIGMA-PHI-V":
         {
            "column": 32,
            "attrs":
            {
               "FIELDNAM": "sigma-phi-V",
               "SCALEMAX": 90.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": 0.00000,
               "CATDESC": "RMS deviation in plasma flow  direction longitude (deg), phi",
               "LABLAXIS": "RMSDev Flow Long",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "Deg",
               "SCALEMIN": 0.00000,
            },
         },
         "BY_GSE":
         {
            "column": 13,
            "attrs":
            {
               "FIELDNAM": "By, GSE",
               "SCALEMAX": 99.90000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": -99.90000,
               "CATDESC": "1AU IP By (nT), GSE",
               "LABLAXIS": "1AU IP By, GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.90000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "nT",
               "SCALEMIN": -99.90000,
            },
         },
         "SIGMA-B":
         {
            "column": 18,
            "attrs":
            {
               "FIELDNAM": "sigma-B",
               "SCALEMAX": 50.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": 0.00000,
               "CATDESC": "RMS deviation of magnitude of the average vector field (nT)",
               "LABLAXIS": "RMSDev Mag Avg B-Vctr",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 50.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "THETA-V":
         {
            "column": 25,
            "attrs":
            {
               "FIELDNAM": "Flow latitude",
               "SCALEMAX": 90.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": -90.00000,
               "CATDESC": "1AU IP plasma flow direction latitude (deg), theta",
               "LABLAXIS": "1AU IP Flow Lat",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "Deg",
               "SCALEMIN": -90.00000,
            },
         },
         "SIGMA-N":
         {
            "column": 30,
            "attrs":
            {
               "FIELDNAM": "sigma-n",
               "SCALEMAX": 80.60000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": 0.00000,
               "CATDESC": "RMS deviation of ion number density (per cc)",
               "LABLAXIS": "RMSDev N(ion)",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 150.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "Per cc",
               "SCALEMIN": 0.00000,
            },
         },
         "AE":
         {
            "column": 41,
            "attrs":
            {
               "FIELDNAM": "AE-index (1-h)",
               "SCALEMAX": 7000.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "I4",
               "VALIDMIN": 0.00000,
               "CATDESC": "AE - 1-hour AE-index (1963/001-1988/182), Provisional (1990/001-2015/212), from WDC Kyoto",
               "LABLAXIS": "1-h AE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 7000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.00000,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "DST":
         {
            "column": 40,
            "attrs":
            {
               "FIELDNAM": "Dst Index (1-h)",
               "SCALEMAX": 500.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "I5",
               "VALIDMIN": -800.00000,
               "CATDESC": "Dst - 1-hour Dst index (1963/001-2011/365), Provisional Dst (2012/001-2015/090), Quick-look Dst (2015/091-2015/252), from WDC Kyoto",
               "LABLAXIS": "1-h Dst",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 500.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": -800.00000,
            },
         },
         "PLS_PTS":
         {
            "column": 7,
            "attrs":
            {
               "FIELDNAM": "# fine time scale plasma points",
               "SCALEMAX": 998.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "I4",
               "VALIDMIN": 0.00000,
               "CATDESC": "# fine time scale plasma points",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 998.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.00000,
               "LABLAXIS": "No. IP Plasma Pts",
               "SCALEMIN": 0.00000,
            },
         },
         "IMF_PTS":
         {
            "column": 6,
            "attrs":
            {
               "FIELDNAM": "# fine time scale IMF points",
               "SCALEMAX": 998.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "I4",
               "VALIDMIN": 0.00000,
               "CATDESC": "# fine time scale IMF points",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 998.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.00000,
               "LABLAXIS": "No. IMF Pts",
               "SCALEMIN": 0.00000,
            },
         },
         "PHI_AV":
         {
            "column": 11,
            "attrs":
            {
               "FIELDNAM": "Long. Angle of AV.",
               "SCALEMAX": 360.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU IP Longitude/Phi of average B vector (deg)",
               "LABLAXIS": "1AU IP Long/Phi Avg B",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 360.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "Deg",
               "SCALEMIN": 0.00000,
            },
         },
         "BZ_GSE":
         {
            "column": 14,
            "attrs":
            {
               "FIELDNAM": "Bz, GSE",
               "SCALEMAX": 99.90000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": -99.90000,
               "CATDESC": "1AU IP Bz (nT), GSE",
               "LABLAXIS": "1AU IP Bz, GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.90000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "nT",
               "SCALEMIN": -99.90000,
            },
         },
         "BZ_GSM":
         {
            "column": 16,
            "attrs":
            {
               "FIELDNAM": "Bz, GSM",
               "SCALEMAX": 99.90000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": -99.90000,
               "CATDESC": "1AU IP Bz (nT), GSM",
               "LABLAXIS": "1AU IP Bz, GSM",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.90000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "nT",
               "SCALEMIN": -99.90000,
            },
         },
         "THETA_AV":
         {
            "column": 10,
            "attrs":
            {
               "FIELDNAM": "Lat. Angle of AV.",
               "SCALEMAX": 90.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.1",
               "VALIDMIN": -90.00000,
               "CATDESC": "1AU IP Latitude/Theta of average B vector (deg)",
               "LABLAXIS": "1AU IP Lat/Theta  Avg B",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "UNITS": "Deg",
               "SCALEMIN": -90.00000,
            },
         },
         "T":
         {
            "column": 22,
            "attrs":
            {
               "FIELDNAM": "Plasma temperature",
               "SCALEMAX": 9999980.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F8.0",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU IP Plasma Temperature, deg K, (last currently-available OMNI plasma data Sep 23, 2015)",
               "LABLAXIS": "1AU IP Plasma Temp",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 9999980.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999990.00000,
               "UNITS": "Deg K",
               "SCALEMIN": 0.00000,
            },
         },
      },
   },
   "1min":
   {
      "attrs":
      {
         "Discipline": "Space Physics>Interplanetary Studies",
         "TITLE": "Near-Earth Heliosphere Data (OMNI)",
         "TEXT": "5minute averaged definitive multispacecraft interplanetary parameters data Additional information for all parameters are available from OMNI Data Documentation: http://omniweb.gsfc.nasa.gov/html/HROdocum.html Additional data access options available at  SPDF's OMNIWeb Service: http://omniweb.gsfc.nasa.gov/ow_min.html Recent omni high resolution updates Release Notes: http://omniweb.gsfc.nasa.gov/html/hro_news.html",
         "LINK_TEXT": "Additional information for all parameters are available from  Additional data access options available at  Recent omni high resolution updates ",
         "alt_logical_source": "Combined_OMNI_1AU-MagneticField-Plasma-HRO_5min_cdf",
         "Instrument_type": "Plasma and Solar Wind Magnetic Fields (space) Electric Fields (space)",
         "MODS": "created November 2006; conversion to ISTP/IACG CDFs via SKTEditor Feb 2000 Time tags in CDAWeb version were modified in March 2005 to use the CDAWeb convention of having mid-average time tags rather than OMNI's original convention of start-of-average time tags.",
         "Source_name": "OMNI (1AU IP Data)>Merged 5 minute Interplantary OMNI data",
         "ADID_ref": "NSSD0110",
         "Logical_file_id": "omni_hro_5min_00000000_v01",
         "Acknowledgement": "NSSDC",
         "Generated_by": "King/Papatashvilli",
         "Project": "NSSDC",
         "Descriptor": "IMF, Plasma, Indices, Energetic Proton Flux",
         "Logical_source_description": "OMNI Combined, Definitive, 5-minute IMF and Plasma, and Energetic Proton Fluxes, Time-Shifted to the Nose  of the Earth's Bow Shock, plus Magnetic Indices",
         "PI_affiliation": "AdnetSystems, NASA GSFC",
         "Generation_date": "Ongoing",
         "Rules_of_use": "Public",
         "LINK_TITLE": "OMNI Data documentation SPDF's OMNIWeb Service Release Notes",
         "HTTP_LINK": "http://omniweb.gsfc.nasa.gov/html/HROdocum.html http://omniweb.gsfc.nasa.gov/ow_min.html http://omniweb.gsfc.nasa.gov/html/hro_news.html",
         "Mission_group": "OMNI (Combined 1AU IP Data; Magnetic and Solar Indices) ACE Wind IMP (All) !___Interplanetary Data near 1 AU",
         "Data_type": "HRO>Definitive 5minute",
         "Data_version": "1",
         "Time_resolution": "5 minute",
         "spase_DatasetResourceID": "spase://VMO/NumericalData/OMNI/PT5M",
         "PI_name": "J.H. King, N. Papatashvilli",
         "Logical_source": "omni_hro_5min",
      },
      "vars":
      {
         "AL_INDEX":
         {
            "column": 38,
            "attrs":
            {
               "FIELDNAM": "AL-index (5-m)",
               "SCALEMAX": 300.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I5",
               "VALIDMIN": -5000.00000,
               "CATDESC": "AL - 5-minute AL-index, from WDC Kyoto (Final 1981/001-1988/366, Provisional 1989/001-2015/334)",
               "LABLAXIS": "5-m AL-index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 300.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": -5000.00000,
            },
         },
         "AE_INDEX":
         {
            "column": 37,
            "attrs":
            {
               "FIELDNAM": "AE-index",
               "SCALEMAX": 7000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I5",
               "VALIDMIN": 0.00000,
               "CATDESC": "AE - 5-minute AE-index, from WDC Kyoto (Final 1981/001-1988/366, Provisional 1989/001-2015/334)",
               "LABLAXIS": "5-m AE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 7000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "y":
         {
            "column": 32,
            "attrs":
            {
               "FIELDNAM": "y (s/c), GSE",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -100.00000,
               "CATDESC": "Y s/c (Re), GSE",
               "LABLAXIS": "y (s/c), GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "Re",
               "SCALEMIN": -100.00000,
            },
         },
         "PR-FLX_10":
         {
            "column": -1,
            "attrs":
            {
               "FIELDNAM": "PROT Flux >10 MEV",
               "SCALEMAX": 90000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F10.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "Proton flux >10 MeV (1/(SQcm-ster-s)) (all fluxes from GOES 1986/001-2016/144)",
               "LABLAXIS": "Protons>10 MeV",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.99219,
               "UNITS": "1/(SQcm-ster-s)",
               "SCALETYP": "log",
               "SCALEMIN": 0.00000,
            },
         },
         "AU_INDEX":
         {
            "column": 39,
            "attrs":
            {
               "FIELDNAM": "AU-index (5-m)",
               "SCALEMAX": 3000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I6",
               "VALIDMIN": -200.00000,
               "CATDESC": "AU - 5-minute AU-index,from WDC Kyoto  (Final 1981/001-1988/366, Provisional 1989/001-2015/334)",
               "LABLAXIS": "AU-index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 3000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": -200.00000,
            },
         },
         "RMS_SD_B":
         {
            "column": 19,
            "attrs":
            {
               "FIELDNAM": "RMS SD B scalar",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "RMS SD B scalar (nT)",
               "LABLAXIS": "RMS SD B scalar",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "Beta":
         {
            "column": 29,
            "attrs":
            {
               "FIELDNAM": "Plasma beta",
               "SCALEMAX": 500.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F6.2",
               "VALIDMIN": 0.00000,
               "VAR_NOTES": "Derived parameters are obtained from the following equations. Plasma beta = [(T*4.16/10**5) + 5.34] * Np / B**2 (B in nT) ",
               "CATDESC": "Plasma beta",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 500.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.98999,
               "LABLAXIS": "Plasma Beta",
               "SCALEMIN": 0.00000,
            },
         },
         "Mach_num":
         {
            "column": 30,
            "attrs":
            {
               "FIELDNAM": "Alfen mach number",
               "SCALEMAX": 500.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F5.1",
               "VALIDMIN": 0.00000,
               "VAR_NOTES": "Derived parameters are obtained from the following equations. Alfven Mach number = (V * Np**0.5) / 20 * B",
               "CATDESC": "Alfven mach number",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 500.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "LABLAXIS": "Alfven Mach No.",
               "SCALEMIN": 0.00000,
            },
         },
         "Pressure":
         {
            "column": 27,
            "attrs":
            {
               "FIELDNAM": "Flow pressure",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F5.2",
               "VALIDMIN": 0.00000,
               "VAR_NOTES": "Derived parameters are obtained from the following equations. Flow pressure = (2*10**-6)*Np*Vp**2 nPa (Np in cm**-3, Vp in km/s, subscript p for proton) ",
               "CATDESC": "Flow pressure (nPa)",
               "LABLAXIS": "Flow pressure",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99.99000,
               "UNITS": "nPa",
               "SCALEMIN": 0.00000,
            },
         },
         "BSN_x":
         {
            "column": 34,
            "attrs":
            {
               "FIELDNAM": "x (BSN), GSE",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -100.00000,
               "CATDESC": "Bow Shock Nose (Re) location, X, GSE",
               "LABLAXIS": "x (BSN), GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "Re",
               "SCALEMIN": -100.00000,
            },
         },
         "Day":
         {
            "column": 1,
            "attrs":
            {
               "FIELDNAM": "Decimal Day (JAN 1=1)",
               "SCALEMAX": 366.00000,
               "VAR_TYPE": "support_data",
               "FORMAT": "I3",
               "VALIDMIN": 1.00000,
               "CATDESC": "Decimal Day",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 366.00000,
               "FILLVAL": -2147483648.00000,
               "LABLAXIS": "Day",
               "SCALEMIN": 1.00000,
            },
         },
         "IMF":
         {
            "column": 4,
            "attrs":
            {
               "FIELDNAM": "ID for IMF spacecraft",
               "SCALEMAX": 98.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I2",
               "VALIDMIN": 1.00000,
               "VAR_NOTES": "The following spacecraft ID's are used: ACE 71, Geotail 60, IMP 8 50, Wind 51 ",
               "CATDESC": "OMNI ID code for the source spacecraft for time-shifted IMF values (see OMNI documentation link for codes)",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 98.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99.00000,
               "LABLAXIS": "IMF S/C ID#",
               "SCALEMIN": 1.00000,
            },
         },
         "T":
         {
            "column": 26,
            "attrs":
            {
               "FIELDNAM": "temperature",
               "SCALEMAX": 9999980.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F8.0",
               "VALIDMIN": 0.00000,
               "CATDESC": "Temperature (K)",
               "LABLAXIS": "temperature",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 9999980.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999999.00000,
               "UNITS": "K",
               "SCALEMIN": 0.00000,
            },
         },
         "BX_GSE":
         {
            "column": 14,
            "attrs":
            {
               "FIELDNAM": "Bx, GSE",
               "SCALEMAX": 99.90000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -99.90000,
               "CATDESC": "Bx (nT), GSE",
               "LABLAXIS": "Bx, GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.90000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": -99.90000,
            },
         },
         "PLS":
         {
            "column": 5,
            "attrs":
            {
               "FIELDNAM": "ID for SW Plasma spacecraft",
               "SCALEMAX": 98.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I2",
               "VALIDMIN": 1.00000,
               "VAR_NOTES": "The following spacecraft ID's are used: ACE 71, Geotail 60, IMP 8 50, Wind 51 ",
               "CATDESC": "OMNI ID code for the source spacecraft for time-shifted IP plasma values (see OMNI documentation link for codes)",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 98.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99.00000,
               "LABLAXIS": "Plasma S/C ID#",
               "SCALEMIN": 1.00000,
            },
         },
         "percent_interp":
         {
            "column": 8,
            "attrs":
            {
               "FIELDNAM": "Percent interpolated",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I3",
               "VALIDMIN": 0.00000,
               "VAR_NOTES": "The percent (0-100) of the points contributing to the 1-min magnetic field averages whose phase front normal (PFN) was interpolated because neither the MVAB-0 nor Cross Product shift techniques yielded a PFN that satisfied its respective tests.",
               "CATDESC": "Percent interpolated",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.00000,
               "LABLAXIS": "Percent interp",
               "SCALEMIN": 0.00000,
            },
         },
         "BZ_GSM":
         {
            "column": 18,
            "attrs":
            {
               "FIELDNAM": "Bz, GSM",
               "SCALEMAX": 99.90000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -99.90000,
               "CATDESC": "Bz (nT), GSM, determined from post-shift GSE components",
               "LABLAXIS": "Bz, GSM",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.90000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": -99.90000,
            },
         },
         "BY_GSE":
         {
            "column": 15,
            "attrs":
            {
               "FIELDNAM": "By, GSE",
               "SCALEMAX": 99.90000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -99.90000,
               "CATDESC": "By (nT), GSE",
               "LABLAXIS": "By, GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.90000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": -99.90000,
            },
         },
         "Time_btwn_obs":
         {
            "column": 12,
            "attrs":
            {
               "FIELDNAM": "Time between obs",
               "SCALEMAX": 10000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I6",
               "VALIDMIN": -10000.00000,
               "CATDESC": "Time between observations (seconds)",
               "LABLAXIS": "Time between obs",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 10000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999999.00000,
               "UNITS": "seconds",
               "SCALEMIN": -10000.00000,
            },
         },
         "x":
         {
            "column": 31,
            "attrs":
            {
               "FIELDNAM": "x (s/c), GSE",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -100.00000,
               "CATDESC": "X s/c (Re), GSE",
               "LABLAXIS": "x (s/c), GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "Re",
               "SCALEMIN": -100.00000,
            },
         },
         "BY_GSM":
         {
            "column": 17,
            "attrs":
            {
               "FIELDNAM": "By, GSM",
               "SCALEMAX": 99.90000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -99.90000,
               "CATDESC": "By (nT), GSM, determined from post-shift GSE components",
               "LABLAXIS": "By, GSM",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.90000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": -99.90000,
            },
         },
         "HR":
         {
            "column": 2,
            "attrs":
            {
               "FIELDNAM": "Decimal Hour",
               "SCALEMAX": 23.00000,
               "VAR_TYPE": "support_data",
               "FORMAT": "I2",
               "VALIDMIN": 0.00000,
               "CATDESC": "Decimal Hour",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 23.00000,
               "FILLVAL": -2147483648.00000,
               "LABLAXIS": "Hour",
               "SCALEMIN": 0.00000,
            },
         },
         "RMS_SD_fld_vec":
         {
            "column": 20,
            "attrs":
            {
               "FIELDNAM": "RMS SD field vector",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": 0.00000,
               "VAR_NOTES": "Note that standard deviations for the two vectors are given as the square roots of the sum of squares of the standard deviations in the component averages.  The component averages are given in the records but not their individual standard deviations.",
               "CATDESC": "RMS SD field vector (nT)",
               "LABLAXIS": "RMS SD field vector",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "Mgs_mach_num":
         {
            "column": 45,
            "attrs":
            {
               "FIELDNAM": "Magnetosonic mach number",
               "SCALEMAX": 30.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F4.1",
               "VALIDMIN": 0.00000,
               "VAR_NOTES": "Derived parameters are obtained from the following equations. Magnetosonic Mach number = V/Magnetosonic_speedMagnetosonic speed = [(sound speed)**2 + (Alfv speed)**2]**0.5The Alfven speed = 20. * B / N**0.5The sound speed = 0.12 * [T + 1.28*10**5]**0.5",
               "CATDESC": "1AU IP Magnetosonic mach number",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 30.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99.90000,
               "LABLAXIS": "1AU IP Magnetosonic  Mach No.",
               "SCALEMIN": 0.00000,
            },
         },
         "PR-FLX_30":
         {
            "column": -1,
            "attrs":
            {
               "FIELDNAM": "PROT Flux >30 MEV",
               "SCALEMAX": 90000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F10.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "Proton flux >30 MeV (1/(SQcm-ster-s))",
               "LABLAXIS": "Protons>30 MeV",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.99219,
               "UNITS": "1/(SQcm-ster-s)",
               "SCALETYP": "log",
               "SCALEMIN": 0.00000,
            },
         },
         "YR":
         {
            "column": 0,
            "attrs":
            {
               "FIELDNAM": "Year",
               "SCALEMAX": 2020.00000,
               "VAR_TYPE": "support_data",
               "FORMAT": "I4",
               "VALIDMIN": 1963.00000,
               "CATDESC": "Year",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 2020.00000,
               "FILLVAL": -2147483648.00000,
               "LABLAXIS": "Year",
               "SCALEMIN": 1963.00000,
            },
         },
         "proton_density":
         {
            "column": 25,
            "attrs":
            {
               "FIELDNAM": "Proton density",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F6.2",
               "VALIDMIN": -100.00000,
               "CATDESC": "Proton density (n/cc) (last currently-available OMNI plasma data May 06, 2016)",
               "LABLAXIS": "Proton density",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.98999,
               "UNITS": "n/cc",
               "SCALEMIN": -100.00000,
            },
         },
         "F":
         {
            "column": 13,
            "attrs":
            {
               "FIELDNAM": "Magnitude of avg. field vector",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "Magnitude of avg. field vector (nT) (last currently-available OMNI B-field data May 06, 2016)",
               "LABLAXIS": "Mag Avg B-vector",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "RMS_Timeshift":
         {
            "column": 10,
            "attrs":
            {
               "FIELDNAM": "RMS Timeshift",
               "SCALEMAX": 10000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I6",
               "VALIDMIN": -10000.00000,
               "CATDESC": "RMS Timeshift (seconds)",
               "LABLAXIS": "RMS Timeshift",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 10000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999999.00000,
               "UNITS": "seconds",
               "SCALEMIN": -10000.00000,
            },
         },
         "PC_N_INDEX":
         {
            "column": 44,
            "attrs":
            {
               "FIELDNAM": "PC(N) index",
               "SCALEMAX": 25.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -5.00000,
               "CATDESC": "PC - 5-minute Polar Cap index (North, Qaanaaq geomagnetic observatory), from DTU Space, Technical University of Denmark (1981/001-2014/365)",
               "LABLAXIS": "5-m PC(N)-index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 25.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.98999,
               "UNITS": " ",
               "SCALEMIN": -5.00000,
            },
         },
         "Minute":
         {
            "column": 3,
            "attrs":
            {
               "FIELDNAM": "Decimal Hour",
               "SCALEMAX": 23.00000,
               "VAR_TYPE": "support_data",
               "FORMAT": "I2",
               "VALIDMIN": 0.00000,
               "CATDESC": "Decimal Hour",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 23.00000,
               "FILLVAL": -2147483648.00000,
               "LABLAXIS": "Hour",
               "SCALEMIN": 0.00000,
            },
         },
         "E":
         {
            "column": 28,
            "attrs":
            {
               "FIELDNAM": "Electric Field",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F6.2",
               "VALIDMIN": -50.00000,
               "VAR_NOTES": "Derived parameters are obtained from the following equations. Electric field = -V(km/s) * Bz (nT; GSM) * 10**-3 ",
               "CATDESC": " Electric Field (mV/m)",
               "LABLAXIS": "Electric Field",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.98999,
               "UNITS": "mV/m",
               "SCALEMIN": -50.00000,
            },
         },
         "SYM_H":
         {
            "column": 41,
            "attrs":
            {
               "FIELDNAM": "SYM/H index",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I5",
               "VALIDMIN": -1000.00000,
               "CATDESC": "SYM/H - 5-minute SYM/H index,from WDC Kyoto (1981/001-2016/091)",
               "LABLAXIS": "SYM/H index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": -1000.00000,
            },
         },
         "SYM_D":
         {
            "column": 40,
            "attrs":
            {
               "FIELDNAM": "SYM/D index",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I5",
               "VALIDMIN": -1000.00000,
               "CATDESC": "SYM/D - 5-minute SYM/D index,from WDC Kyoto (1981/001-2016/091)",
               "LABLAXIS": "SYM/D index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": -1000.00000,
            },
         },
         "PLS_PTS":
         {
            "column": 7,
            "attrs":
            {
               "FIELDNAM": "# fine time scale plasma averages",
               "SCALEMAX": 998.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I3",
               "VALIDMIN": 0.00000,
               "CATDESC": "Number of fine time scale points in plasma averages",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 998.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.00000,
               "LABLAXIS": "No. IP Plasma avg",
               "SCALEMIN": 0.00000,
            },
         },
         "flow_speed":
         {
            "column": 21,
            "attrs":
            {
               "FIELDNAM": "Flow speed",
               "SCALEMAX": 1200.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.0",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU IP plasma flow speed (km/s)",
               "LABLAXIS": "1AU IP Plasma Speed",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1200.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.90000,
               "UNITS": "Km/s",
               "SCALEMIN": 0.00000,
            },
         },
         "BSN_y":
         {
            "column": 35,
            "attrs":
            {
               "FIELDNAM": "y (BSN), GSE",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -100.00000,
               "CATDESC": "Bow Shock Nose (Re) location, Y, GSE",
               "LABLAXIS": "y (BSN), GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "Re",
               "SCALEMIN": -100.00000,
            },
         },
         "IMF_PTS":
         {
            "column": 6,
            "attrs":
            {
               "FIELDNAM": "# fine time scale IMF averages",
               "SCALEMAX": 998.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I3",
               "VALIDMIN": 0.00000,
               "CATDESC": "Number of fine time scale points in IMF averages",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 998.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.00000,
               "LABLAXIS": "No. IMF avg",
               "SCALEMIN": 0.00000,
            },
         },
         "BSN_z":
         {
            "column": 36,
            "attrs":
            {
               "FIELDNAM": "z (BSN), GSE",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -100.00000,
               "CATDESC": "Bow Shock Nose (Re) location, Z, GSE",
               "LABLAXIS": "z (BSN), GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "Re",
               "SCALEMIN": -100.00000,
            },
         },
         "BZ_GSE":
         {
            "column": 16,
            "attrs":
            {
               "FIELDNAM": "Bz, GSE",
               "SCALEMAX": 99.90000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -99.90000,
               "CATDESC": "Bz (nT), GSE",
               "LABLAXIS": "Bz, GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.90000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": -99.90000,
            },
         },
         "ASY_H":
         {
            "column": 43,
            "attrs":
            {
               "FIELDNAM": "ASY/H index",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I5",
               "VALIDMIN": -1000.00000,
               "CATDESC": "ASY/H - 5-minute ASY/H index,from WDC Kyoto (1981/001-2016/091)",
               "LABLAXIS": "ASY/H index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": -1000.00000,
            },
         },
         "z":
         {
            "column": 33,
            "attrs":
            {
               "FIELDNAM": "z (s/c), GSE",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -100.00000,
               "CATDESC": "Z s/c (Re), GSE",
               "LABLAXIS": "z (s/c), GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "Re",
               "SCALEMIN": -100.00000,
            },
         },
         "Timeshift":
         {
            "column": 9,
            "attrs":
            {
               "FIELDNAM": "Timeshift",
               "SCALEMAX": 10000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I6",
               "VALIDMIN": -10000.00000,
               "CATDESC": "Timeshift (seconds)",
               "LABLAXIS": "Timeshift",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 10000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999999.00000,
               "UNITS": "seconds",
               "SCALEMIN": -10000.00000,
            },
         },
         "ASY_D":
         {
            "column": 42,
            "attrs":
            {
               "FIELDNAM": "ASY/D index",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I5",
               "VALIDMIN": -1000.00000,
               "CATDESC": "ASY/D - 5-minute ASY/D index,from WDC Kyoto (1981/001-2016/091)",
               "LABLAXIS": "ASY/D index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": -1000.00000,
            },
         },
         "Vx":
         {
            "column": 22,
            "attrs":
            {
               "FIELDNAM": "Vx Velocity, GSE",
               "SCALEMAX": 2000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.1",
               "VALIDMIN": -2000.00000,
               "CATDESC": "Vx Velocity (km/s), GSE",
               "LABLAXIS": "Vx Velocity, GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 2000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.89844,
               "UNITS": "km/s",
               "SCALEMIN": -2000.00000,
            },
         },
         "Vy":
         {
            "column": 23,
            "attrs":
            {
               "FIELDNAM": "Vy Velocity, GSE",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.1",
               "VALIDMIN": -1000.00000,
               "CATDESC": "Vy Velocity (km/s), GSE",
               "LABLAXIS": "Vy Velocity, GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.89844,
               "UNITS": "km/s",
               "SCALEMIN": -1000.00000,
            },
         },
         "Vz":
         {
            "column": 24,
            "attrs":
            {
               "FIELDNAM": "Vz Velocity, GSE",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.1",
               "VALIDMIN": -100.00000,
               "CATDESC": "Vz Velocity (km/s), GSE",
               "LABLAXIS": "Vz Velocity, GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.89844,
               "UNITS": "km/s",
               "SCALEMIN": -100.00000,
            },
         },
         "PR-FLX_60":
         {
            "column": -1,
            "attrs":
            {
               "FIELDNAM": "PROT Flux >60 MEV",
               "SCALEMAX": 90000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F10.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "Proton flux >60 MeV (1/(SQcm-ster-s))",
               "LABLAXIS": "Protons>60 MeV",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.99219,
               "UNITS": "1/(SQcm-ster-s)..",
               "SCALETYP": "log",
               "SCALEMIN": 0.00000,
            },
         },
      },
   },
   "5min":
   {
      "attrs":
      {
         "Discipline": "Space Physics>Interplanetary Studies",
         "TITLE": "Near-Earth Heliosphere Data (OMNI)",
         "TEXT": "5minute averaged definitive multispacecraft interplanetary parameters data Additional information for all parameters are available from OMNI Data Documentation: http://omniweb.gsfc.nasa.gov/html/HROdocum.html Additional data access options available at  SPDF's OMNIWeb Service: http://omniweb.gsfc.nasa.gov/ow_min.html Recent omni high resolution updates Release Notes: http://omniweb.gsfc.nasa.gov/html/hro_news.html",
         "LINK_TEXT": "Additional information for all parameters are available from  Additional data access options available at  Recent omni high resolution updates ",
         "alt_logical_source": "Combined_OMNI_1AU-MagneticField-Plasma-HRO_5min_cdf",
         "Instrument_type": "Plasma and Solar Wind Magnetic Fields (space) Electric Fields (space)",
         "MODS": "created November 2006; conversion to ISTP/IACG CDFs via SKTEditor Feb 2000 Time tags in CDAWeb version were modified in March 2005 to use the CDAWeb convention of having mid-average time tags rather than OMNI's original convention of start-of-average time tags.",
         "Source_name": "OMNI (1AU IP Data)>Merged 5 minute Interplantary OMNI data",
         "ADID_ref": "NSSD0110",
         "Logical_file_id": "omni_hro_5min_00000000_v01",
         "Acknowledgement": "NSSDC",
         "Generated_by": "King/Papatashvilli",
         "Project": "NSSDC",
         "Descriptor": "IMF, Plasma, Indices, Energetic Proton Flux",
         "Logical_source_description": "OMNI Combined, Definitive, 5-minute IMF and Plasma, and Energetic Proton Fluxes, Time-Shifted to the Nose  of the Earth's Bow Shock, plus Magnetic Indices",
         "PI_affiliation": "AdnetSystems, NASA GSFC",
         "Generation_date": "Ongoing",
         "Rules_of_use": "Public",
         "LINK_TITLE": "OMNI Data documentation SPDF's OMNIWeb Service Release Notes",
         "HTTP_LINK": "http://omniweb.gsfc.nasa.gov/html/HROdocum.html http://omniweb.gsfc.nasa.gov/ow_min.html http://omniweb.gsfc.nasa.gov/html/hro_news.html",
         "Mission_group": "OMNI (Combined 1AU IP Data; Magnetic and Solar Indices) ACE Wind IMP (All) !___Interplanetary Data near 1 AU",
         "Data_type": "HRO>Definitive 5minute",
         "Data_version": "1",
         "Time_resolution": "5 minute",
         "spase_DatasetResourceID": "spase://VMO/NumericalData/OMNI/PT5M",
         "PI_name": "J.H. King, N. Papatashvilli",
         "Logical_source": "omni_hro_5min",
      },
      "vars":
      {
         "AL_INDEX":
         {
            "column": 38,
            "attrs":
            {
               "FIELDNAM": "AL-index (5-m)",
               "SCALEMAX": 300.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I5",
               "VALIDMIN": -5000.00000,
               "CATDESC": "AL - 5-minute AL-index, from WDC Kyoto (Final 1981/001-1988/366, Provisional 1989/001-2015/334)",
               "LABLAXIS": "5-m AL-index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 300.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": -5000.00000,
            },
         },
         "AE_INDEX":
         {
            "column": 37,
            "attrs":
            {
               "FIELDNAM": "AE-index",
               "SCALEMAX": 7000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I5",
               "VALIDMIN": 0.00000,
               "CATDESC": "AE - 5-minute AE-index, from WDC Kyoto (Final 1981/001-1988/366, Provisional 1989/001-2015/334)",
               "LABLAXIS": "5-m AE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 7000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "y":
         {
            "column": 32,
            "attrs":
            {
               "FIELDNAM": "y (s/c), GSE",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -100.00000,
               "CATDESC": "Y s/c (Re), GSE",
               "LABLAXIS": "y (s/c), GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "Re",
               "SCALEMIN": -100.00000,
            },
         },
         "PR-FLX_10":
         {
            "column": -1,
            "attrs":
            {
               "FIELDNAM": "PROT Flux >10 MEV",
               "SCALEMAX": 90000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F10.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "Proton flux >10 MeV (1/(SQcm-ster-s)) (all fluxes from GOES 1986/001-2016/144)",
               "LABLAXIS": "Protons>10 MeV",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.99219,
               "UNITS": "1/(SQcm-ster-s)",
               "SCALETYP": "log",
               "SCALEMIN": 0.00000,
            },
         },
         "AU_INDEX":
         {
            "column": 39,
            "attrs":
            {
               "FIELDNAM": "AU-index (5-m)",
               "SCALEMAX": 3000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I6",
               "VALIDMIN": -200.00000,
               "CATDESC": "AU - 5-minute AU-index,from WDC Kyoto  (Final 1981/001-1988/366, Provisional 1989/001-2015/334)",
               "LABLAXIS": "AU-index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 3000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": -200.00000,
            },
         },
         "RMS_SD_B":
         {
            "column": 19,
            "attrs":
            {
               "FIELDNAM": "RMS SD B scalar",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "RMS SD B scalar (nT)",
               "LABLAXIS": "RMS SD B scalar",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "Beta":
         {
            "column": 29,
            "attrs":
            {
               "FIELDNAM": "Plasma beta",
               "SCALEMAX": 500.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F6.2",
               "VALIDMIN": 0.00000,
               "VAR_NOTES": "Derived parameters are obtained from the following equations. Plasma beta = [(T*4.16/10**5) + 5.34] * Np / B**2 (B in nT) ",
               "CATDESC": "Plasma beta",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 500.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.98999,
               "LABLAXIS": "Plasma Beta",
               "SCALEMIN": 0.00000,
            },
         },
         "Mach_num":
         {
            "column": 30,
            "attrs":
            {
               "FIELDNAM": "Alfen mach number",
               "SCALEMAX": 500.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F5.1",
               "VALIDMIN": 0.00000,
               "VAR_NOTES": "Derived parameters are obtained from the following equations. Alfven Mach number = (V * Np**0.5) / 20 * B",
               "CATDESC": "Alfven mach number",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 500.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.90002,
               "LABLAXIS": "Alfven Mach No.",
               "SCALEMIN": 0.00000,
            },
         },
         "Pressure":
         {
            "column": 27,
            "attrs":
            {
               "FIELDNAM": "Flow pressure",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F5.2",
               "VALIDMIN": 0.00000,
               "VAR_NOTES": "Derived parameters are obtained from the following equations. Flow pressure = (2*10**-6)*Np*Vp**2 nPa (Np in cm**-3, Vp in km/s, subscript p for proton) ",
               "CATDESC": "Flow pressure (nPa)",
               "LABLAXIS": "Flow pressure",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99.99000,
               "UNITS": "nPa",
               "SCALEMIN": 0.00000,
            },
         },
         "BSN_x":
         {
            "column": 34,
            "attrs":
            {
               "FIELDNAM": "x (BSN), GSE",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -100.00000,
               "CATDESC": "Bow Shock Nose (Re) location, X, GSE",
               "LABLAXIS": "x (BSN), GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "Re",
               "SCALEMIN": -100.00000,
            },
         },
         "Day":
         {
            "column": 1,
            "attrs":
            {
               "FIELDNAM": "Decimal Day (JAN 1=1)",
               "SCALEMAX": 366.00000,
               "VAR_TYPE": "support_data",
               "FORMAT": "I3",
               "VALIDMIN": 1.00000,
               "CATDESC": "Decimal Day",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 366.00000,
               "FILLVAL": -2147483648.00000,
               "LABLAXIS": "Day",
               "SCALEMIN": 1.00000,
            },
         },
         "IMF":
         {
            "column": 4,
            "attrs":
            {
               "FIELDNAM": "ID for IMF spacecraft",
               "SCALEMAX": 98.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I2",
               "VALIDMIN": 1.00000,
               "VAR_NOTES": "The following spacecraft ID's are used: ACE 71, Geotail 60, IMP 8 50, Wind 51 ",
               "CATDESC": "OMNI ID code for the source spacecraft for time-shifted IMF values (see OMNI documentation link for codes)",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 98.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99.00000,
               "LABLAXIS": "IMF S/C ID#",
               "SCALEMIN": 1.00000,
            },
         },
         "T":
         {
            "column": 26,
            "attrs":
            {
               "FIELDNAM": "temperature",
               "SCALEMAX": 9999980.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F8.0",
               "VALIDMIN": 0.00000,
               "CATDESC": "Temperature (K)",
               "LABLAXIS": "temperature",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 9999980.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999999.00000,
               "UNITS": "K",
               "SCALEMIN": 0.00000,
            },
         },
         "BX_GSE":
         {
            "column": 14,
            "attrs":
            {
               "FIELDNAM": "Bx, GSE",
               "SCALEMAX": 99.90000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -99.90000,
               "CATDESC": "Bx (nT), GSE",
               "LABLAXIS": "Bx, GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.90000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": -99.90000,
            },
         },
         "PLS":
         {
            "column": 5,
            "attrs":
            {
               "FIELDNAM": "ID for SW Plasma spacecraft",
               "SCALEMAX": 98.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I2",
               "VALIDMIN": 1.00000,
               "VAR_NOTES": "The following spacecraft ID's are used: ACE 71, Geotail 60, IMP 8 50, Wind 51 ",
               "CATDESC": "OMNI ID code for the source spacecraft for time-shifted IP plasma values (see OMNI documentation link for codes)",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 98.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99.00000,
               "LABLAXIS": "Plasma S/C ID#",
               "SCALEMIN": 1.00000,
            },
         },
         "percent_interp":
         {
            "column": 8,
            "attrs":
            {
               "FIELDNAM": "Percent interpolated",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I3",
               "VALIDMIN": 0.00000,
               "VAR_NOTES": "The percent (0-100) of the points contributing to the 1-min magnetic field averages whose phase front normal (PFN) was interpolated because neither the MVAB-0 nor Cross Product shift techniques yielded a PFN that satisfied its respective tests.",
               "CATDESC": "Percent interpolated",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.00000,
               "LABLAXIS": "Percent interp",
               "SCALEMIN": 0.00000,
            },
         },
         "BZ_GSM":
         {
            "column": 18,
            "attrs":
            {
               "FIELDNAM": "Bz, GSM",
               "SCALEMAX": 99.90000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -99.90000,
               "CATDESC": "Bz (nT), GSM, determined from post-shift GSE components",
               "LABLAXIS": "Bz, GSM",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.90000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": -99.90000,
            },
         },
         "BY_GSE":
         {
            "column": 15,
            "attrs":
            {
               "FIELDNAM": "By, GSE",
               "SCALEMAX": 99.90000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -99.90000,
               "CATDESC": "By (nT), GSE",
               "LABLAXIS": "By, GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.90000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": -99.90000,
            },
         },
         "Time_btwn_obs":
         {
            "column": 12,
            "attrs":
            {
               "FIELDNAM": "Time between obs",
               "SCALEMAX": 10000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I6",
               "VALIDMIN": -10000.00000,
               "CATDESC": "Time between observations (seconds)",
               "LABLAXIS": "Time between obs",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 10000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999999.00000,
               "UNITS": "seconds",
               "SCALEMIN": -10000.00000,
            },
         },
         "x":
         {
            "column": 31,
            "attrs":
            {
               "FIELDNAM": "x (s/c), GSE",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -100.00000,
               "CATDESC": "X s/c (Re), GSE",
               "LABLAXIS": "x (s/c), GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "Re",
               "SCALEMIN": -100.00000,
            },
         },
         "BY_GSM":
         {
            "column": 17,
            "attrs":
            {
               "FIELDNAM": "By, GSM",
               "SCALEMAX": 99.90000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -99.90000,
               "CATDESC": "By (nT), GSM, determined from post-shift GSE components",
               "LABLAXIS": "By, GSM",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.90000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": -99.90000,
            },
         },
         "HR":
         {
            "column": 2,
            "attrs":
            {
               "FIELDNAM": "Decimal Hour",
               "SCALEMAX": 23.00000,
               "VAR_TYPE": "support_data",
               "FORMAT": "I2",
               "VALIDMIN": 0.00000,
               "CATDESC": "Decimal Hour",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 23.00000,
               "FILLVAL": -2147483648.00000,
               "LABLAXIS": "Hour",
               "SCALEMIN": 0.00000,
            },
         },
         "RMS_SD_fld_vec":
         {
            "column": 20,
            "attrs":
            {
               "FIELDNAM": "RMS SD field vector",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": 0.00000,
               "VAR_NOTES": "Note that standard deviations for the two vectors are given as the square roots of the sum of squares of the standard deviations in the component averages.  The component averages are given in the records but not their individual standard deviations.",
               "CATDESC": "RMS SD field vector (nT)",
               "LABLAXIS": "RMS SD field vector",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "Mgs_mach_num":
         {
            "column": 45,
            "attrs":
            {
               "FIELDNAM": "Magnetosonic mach number",
               "SCALEMAX": 30.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F4.1",
               "VALIDMIN": 0.00000,
               "VAR_NOTES": "Derived parameters are obtained from the following equations. Magnetosonic Mach number = V/Magnetosonic_speedMagnetosonic speed = [(sound speed)**2 + (Alfv speed)**2]**0.5The Alfven speed = 20. * B / N**0.5The sound speed = 0.12 * [T + 1.28*10**5]**0.5",
               "CATDESC": "1AU IP Magnetosonic mach number",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 30.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99.90000,
               "LABLAXIS": "1AU IP Magnetosonic  Mach No.",
               "SCALEMIN": 0.00000,
            },
         },
         "PR-FLX_30":
         {
            "column": -1,
            "attrs":
            {
               "FIELDNAM": "PROT Flux >30 MEV",
               "SCALEMAX": 90000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F10.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "Proton flux >30 MeV (1/(SQcm-ster-s))",
               "LABLAXIS": "Protons>30 MeV",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.99219,
               "UNITS": "1/(SQcm-ster-s)",
               "SCALETYP": "log",
               "SCALEMIN": 0.00000,
            },
         },
         "YR":
         {
            "column": 0,
            "attrs":
            {
               "FIELDNAM": "Year",
               "SCALEMAX": 2020.00000,
               "VAR_TYPE": "support_data",
               "FORMAT": "I4",
               "VALIDMIN": 1963.00000,
               "CATDESC": "Year",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 2020.00000,
               "FILLVAL": -2147483648.00000,
               "LABLAXIS": "Year",
               "SCALEMIN": 1963.00000,
            },
         },
         "proton_density":
         {
            "column": 25,
            "attrs":
            {
               "FIELDNAM": "Proton density",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F6.2",
               "VALIDMIN": -100.00000,
               "CATDESC": "Proton density (n/cc) (last currently-available OMNI plasma data May 06, 2016)",
               "LABLAXIS": "Proton density",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.98999,
               "UNITS": "n/cc",
               "SCALEMIN": -100.00000,
            },
         },
         "F":
         {
            "column": 13,
            "attrs":
            {
               "FIELDNAM": "Magnitude of avg. field vector",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "Magnitude of avg. field vector (nT) (last currently-available OMNI B-field data May 06, 2016)",
               "LABLAXIS": "Mag Avg B-vector",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": 0.00000,
            },
         },
         "RMS_Timeshift":
         {
            "column": 10,
            "attrs":
            {
               "FIELDNAM": "RMS Timeshift",
               "SCALEMAX": 10000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I6",
               "VALIDMIN": -10000.00000,
               "CATDESC": "RMS Timeshift (seconds)",
               "LABLAXIS": "RMS Timeshift",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 10000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999999.00000,
               "UNITS": "seconds",
               "SCALEMIN": -10000.00000,
            },
         },
         "PC_N_INDEX":
         {
            "column": 44,
            "attrs":
            {
               "FIELDNAM": "PC(N) index",
               "SCALEMAX": 25.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -5.00000,
               "CATDESC": "PC - 5-minute Polar Cap index (North, Qaanaaq geomagnetic observatory), from DTU Space, Technical University of Denmark (1981/001-2014/365)",
               "LABLAXIS": "5-m PC(N)-index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 25.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.98999,
               "UNITS": " ",
               "SCALEMIN": -5.00000,
            },
         },
         "Minute":
         {
            "column": 3,
            "attrs":
            {
               "FIELDNAM": "Decimal Hour",
               "SCALEMAX": 23.00000,
               "VAR_TYPE": "support_data",
               "FORMAT": "I2",
               "VALIDMIN": 0.00000,
               "CATDESC": "Decimal Hour",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 23.00000,
               "FILLVAL": -2147483648.00000,
               "LABLAXIS": "Hour",
               "SCALEMIN": 0.00000,
            },
         },
         "E":
         {
            "column": 28,
            "attrs":
            {
               "FIELDNAM": "Electric Field",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F6.2",
               "VALIDMIN": -50.00000,
               "VAR_NOTES": "Derived parameters are obtained from the following equations. Electric field = -V(km/s) * Bz (nT; GSM) * 10**-3 ",
               "CATDESC": " Electric Field (mV/m)",
               "LABLAXIS": "Electric Field",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.98999,
               "UNITS": "mV/m",
               "SCALEMIN": -50.00000,
            },
         },
         "SYM_H":
         {
            "column": 41,
            "attrs":
            {
               "FIELDNAM": "SYM/H index",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I5",
               "VALIDMIN": -1000.00000,
               "CATDESC": "SYM/H - 5-minute SYM/H index,from WDC Kyoto (1981/001-2016/091)",
               "LABLAXIS": "SYM/H index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": -1000.00000,
            },
         },
         "SYM_D":
         {
            "column": 40,
            "attrs":
            {
               "FIELDNAM": "SYM/D index",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I5",
               "VALIDMIN": -1000.00000,
               "CATDESC": "SYM/D - 5-minute SYM/D index,from WDC Kyoto (1981/001-2016/091)",
               "LABLAXIS": "SYM/D index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": -1000.00000,
            },
         },
         "PLS_PTS":
         {
            "column": 7,
            "attrs":
            {
               "FIELDNAM": "# fine time scale plasma averages",
               "SCALEMAX": 998.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I3",
               "VALIDMIN": 0.00000,
               "CATDESC": "Number of fine time scale points in plasma averages",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 998.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.00000,
               "LABLAXIS": "No. IP Plasma avg",
               "SCALEMIN": 0.00000,
            },
         },
         "flow_speed":
         {
            "column": 21,
            "attrs":
            {
               "FIELDNAM": "Flow speed",
               "SCALEMAX": 1200.00000,
               "VAR_TYPE": "ignore_data",
               "FORMAT": "F5.0",
               "VALIDMIN": 0.00000,
               "CATDESC": "1AU IP plasma flow speed (km/s)",
               "LABLAXIS": "1AU IP Plasma Speed",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1200.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.900000,
               "UNITS": "Km/s",
               "SCALEMIN": 0.00000,
            },
         },
         "BSN_y":
         {
            "column": 35,
            "attrs":
            {
               "FIELDNAM": "y (BSN), GSE",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -100.00000,
               "CATDESC": "Bow Shock Nose (Re) location, Y, GSE",
               "LABLAXIS": "y (BSN), GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "Re",
               "SCALEMIN": -100.00000,
            },
         },
         "IMF_PTS":
         {
            "column": 6,
            "attrs":
            {
               "FIELDNAM": "# fine time scale IMF averages",
               "SCALEMAX": 998.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I3",
               "VALIDMIN": 0.00000,
               "CATDESC": "Number of fine time scale points in IMF averages",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 998.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999.00000,
               "LABLAXIS": "No. IMF avg",
               "SCALEMIN": 0.00000,
            },
         },
         "BSN_z":
         {
            "column": 36,
            "attrs":
            {
               "FIELDNAM": "z (BSN), GSE",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -100.00000,
               "CATDESC": "Bow Shock Nose (Re) location, Z, GSE",
               "LABLAXIS": "z (BSN), GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "Re",
               "SCALEMIN": -100.00000,
            },
         },
         "BZ_GSE":
         {
            "column": 16,
            "attrs":
            {
               "FIELDNAM": "Bz, GSE",
               "SCALEMAX": 99.90000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -99.90000,
               "CATDESC": "Bz (nT), GSE",
               "LABLAXIS": "Bz, GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 99.90000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "nT",
               "SCALEMIN": -99.90000,
            },
         },
         "ASY_H":
         {
            "column": 43,
            "attrs":
            {
               "FIELDNAM": "ASY/H index",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I5",
               "VALIDMIN": -1000.00000,
               "CATDESC": "ASY/H - 5-minute ASY/H index,from WDC Kyoto (1981/001-2016/091)",
               "LABLAXIS": "ASY/H index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": -1000.00000,
            },
         },
         "z":
         {
            "column": 33,
            "attrs":
            {
               "FIELDNAM": "z (s/c), GSE",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.2",
               "VALIDMIN": -100.00000,
               "CATDESC": "Z s/c (Re), GSE",
               "LABLAXIS": "z (s/c), GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 9999.99023,
               "UNITS": "Re",
               "SCALEMIN": -100.00000,
            },
         },
         "Timeshift":
         {
            "column": 9,
            "attrs":
            {
               "FIELDNAM": "Timeshift",
               "SCALEMAX": 10000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I6",
               "VALIDMIN": -10000.00000,
               "CATDESC": "Timeshift (seconds)",
               "LABLAXIS": "Timeshift",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 10000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 999999.00000,
               "UNITS": "seconds",
               "SCALEMIN": -10000.00000,
            },
         },
         "ASY_D":
         {
            "column": 42,
            "attrs":
            {
               "FIELDNAM": "ASY/D index",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "I5",
               "VALIDMIN": -1000.00000,
               "CATDESC": "ASY/D - 5-minute ASY/D index,from WDC Kyoto (1981/001-2016/091)",
               "LABLAXIS": "ASY/D index",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.00000,
               "UNITS": "nT",
               "SCALEMIN": -1000.00000,
            },
         },
         "Vx":
         {
            "column": 22,
            "attrs":
            {
               "FIELDNAM": "Vx Velocity, GSE",
               "SCALEMAX": 2000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.1",
               "VALIDMIN": -2000.00000,
               "CATDESC": "Vx Velocity (km/s), GSE",
               "LABLAXIS": "Vx Velocity, GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 2000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.89844,
               "UNITS": "km/s",
               "SCALEMIN": -2000.00000,
            },
         },
         "Vy":
         {
            "column": 23,
            "attrs":
            {
               "FIELDNAM": "Vy Velocity, GSE",
               "SCALEMAX": 1000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.1",
               "VALIDMIN": -1000.00000,
               "CATDESC": "Vy Velocity (km/s), GSE",
               "LABLAXIS": "Vy Velocity, GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 1000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.89844,
               "UNITS": "km/s",
               "SCALEMIN": -1000.00000,
            },
         },
         "Vz":
         {
            "column": 24,
            "attrs":
            {
               "FIELDNAM": "Vz Velocity, GSE",
               "SCALEMAX": 100.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F7.1",
               "VALIDMIN": -100.00000,
               "CATDESC": "Vz Velocity (km/s), GSE",
               "LABLAXIS": "Vz Velocity, GSE",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 100.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.89844,
               "UNITS": "km/s",
               "SCALEMIN": -100.00000,
            },
         },
         "PR-FLX_60":
         {
            "column": -1,
            "attrs":
            {
               "FIELDNAM": "PROT Flux >60 MEV",
               "SCALEMAX": 90000.00000,
               "VAR_TYPE": "data",
               "FORMAT": "F10.2",
               "VALIDMIN": 0.00000,
               "CATDESC": "Proton flux >60 MeV (1/(SQcm-ster-s))",
               "LABLAXIS": "Protons>60 MeV",
               "DEPEND_0": "Epoch",
               "VALIDMAX": 90000.00000,
               "DISPLAY_TYPE": "time_series",
               "FILLVAL": 99999.99219,
               "UNITS": "1/(SQcm-ster-s)..",
               "SCALETYP": "log",
               "SCALEMIN": 0.00000,
            }
         }
      }
   }
}
