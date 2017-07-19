# -*- coding: utf-8 -*-
"""
Common tools for working with COSIMA model output
"""

import numpy as np
import os

import dask
import dask.bag
from dask.distributed import Client

import pandas as pd
import xarray as xr
from glob import glob
import re
import netCDF4

from joblib import Memory

from tqdm import tqdm_notebook, tqdm


client = Client()

# hardcoded -- this is meant to be run on a NCI system
DataDir = '/g/data3/hh5/tmp/cosima'

cachedir = '/g/data1/v45/cosima-cookbook'

memory = Memory(cachedir=cachedir, verbose=0)

import warnings
warnings.filterwarnings("ignore",
                        message="Unable to decode time axis into full numpy.datetime64 objects")

# find all experiments with at least one outputNNN subdirectory
expts = sorted({ re.search(DataDir + '/' + '(.*)' + '/output', d).group(1)
	         for d in glob(os.path.join(DataDir , '*/*/output*') )})

from .netcdf_index import build_index
from .netcdf_index import get_nc_variable

def get_expt():
    cwd = os.getcwd()
    _, expt = cwd.split('cosima-cookbook/configurations/')
    return expt

class Configuration():
    pass

class Experiment():
    def __init__():
        pass
