#!/usr/bin/env python
# coding: utf-8

# In[1]:


import imdlib as imd
import pandas as pd
import matplotlib.pyplot as plt
import xarray 
file_dir=r'C:\Users\Nirdesh\Documents\Untitled Folder'
start_yr=1951
end_yr=1955
variable = 'tmax'
data = imd.open_data(variable, start_yr, end_yr,'yearwise', file_dir)
ds = data.get_xarray()


# In[2]:


min_lon = 75
min_lat = 27
max_lon = 78
max_lat = 29

mask_lon = (ds.lon >= min_lon) & (ds.lon <= max_lon)
mask_lat = (ds.lat >= min_lat) & (ds.lat <= max_lat)
cropped_ds = ds.where(mask_lon & mask_lat, drop=True)
df=cropped_ds.to_dataframe()


# In[3]:



get_ipython().run_line_magic('matplotlib', 'inline')
ds=df.groupby(['time']).mean()
ds.plot()


