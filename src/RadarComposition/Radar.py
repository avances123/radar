#!/usr/bin/env python

'''
Created on 26/10/2010

@author: Fabio Rueda Carrascosa
'''

class Radar(object):
    '''
    classdocs
    '''

    DEFAULT_PROJ = "+proj=lcc +lat_1=46.5 +lat_2=33.5 +lat_0=0 +lon_0=0 +x_0=0 +y_0=0 +ellps=GRS80 +units=m +no_defs"
    LATLONG_PROJ = "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs "
    DEFAULT_PROJ_WKT = 'PROJCS["unnamed",GEOGCS["GRS 1980(IUGG, 1980)",DATUM["unknown",SPHEROID["GRS80",6378137,298.257222101]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic_2SP"],PARAMETER["standard_parallel_1",46.5],PARAMETER["standard_parallel_2",33.5],PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",0],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1,AUTHORITY["EPSG","9001"]]]'
    


    def __init__(self,imagepath):
        '''
        Constructor
        '''
        self.imagepath = imagepath
        

    
    