#!/usr/bin/env python
'''
Created on 26/10/2010

@author: fabio
'''
import gdal
import sys
from Radar import Radar


class Regional(Radar):  # Hereda de Radar
    '''
    classdocs
    '''

# Constructor
    def __init__(self, imagepath, region):
        """
        Crea un RadarRegional a partir de un fichero

        imagepath -- Name of file to read.
        """

        self.imagepath = imagepath
        self.region = region        
        
                     
        self.dataset = gdal.Open(imagepath)
        if self.dataset is None:
            print('Unable to open %s' % imagepath)
            sys.exit(1)
        self.driver = self.dataset.GetDriver()
        #print 'Driver: ' + self.driver.LongName
        self.num_bands = self.dataset.RasterCount
        self.band = self.dataset.GetRasterBand(1) # Solo tiene una banda el gif
        self.colortable = self.band.GetRasterColorTable()
        self.xsize = self.dataset.RasterXSize
        self.ysize = self.dataset.RasterYSize
        self.band_type = self.band.DataType
        #self.projection = self.dataset.GetProjection()
        self.projection = Radar.DEFAULT_PROJ
        self.geotransform = self.dataset.GetGeoTransform()
        self.ulx = self.geotransform[0]
        self.uly = self.geotransform[3]
        self.lrx = self.ulx + self.geotransform[1] * self.xsize
        self.lry = self.uly + self.geotransform[5] * self.ysize

    def getValidColors(self):
        print self.colortable

if __name__ == '__main__':
    from Retriever import Retriever
    retriever = Retriever()
    image_dict = retriever.downloadImages(['ma'])
    for i in image_dict.iterkeys():
        radar = Regional(image_dict[i],i)
        print "Creado radar regional: " + radar.imagepath + ' Region: ' + radar.region
        radar.getValidColors()
        
        
        
        