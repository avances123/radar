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
    

    def __init__(self,imagepath):
        '''
        Constructor
        '''
        self.imagepath = imagepath
        

    
    