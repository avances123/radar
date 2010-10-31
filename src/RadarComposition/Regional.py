#!/usr/bin/env python
'''
Created on 26/10/2010

@author: fabio
'''
try:
    from osgeo import gdal
    from osgeo.gdalconst import *
    gdal.TermProgress = gdal.TermProgress_nocb
except ImportError:
    import gdal
    from gdalconst import *
    
import gdalnumeric

import sys
from Radar import Radar


class Regional(Radar):  # Hereda de Radar
    '''
    classdocs
    '''
    inNoData = None

    def fillData(self,inband):
        data=[]
        for i in range(inband.YSize - 1, -1, -1): #Desde 479 a 0 en pasos de -1
            scanline = inband.ReadAsArray(0, i, inband.XSize, 1, inband.XSize, 1)
            #scanline = numpy.choose( numpy.equal( scanline, inNoData),(scanline, outNoData) )
            data.WriteArray(scanline, 0, i)
        self.data = data   
    
    def printReport(self):
        print('Filename: '+ self.imagepath)
        print('File Size: %dx%dx%d' % (self.xsize, self.ysize, self.num_bands))
        print('Pixel Size: %f x %f' % (self.geotransform[1],self.geotransform[5]))
        print('UL:(%f,%f)   LR:(%f,%f)'  % (self.ulx,self.uly,self.lrx,self.lry))
        print('Projection '  + self.projection)
        print('Band Type: '  + str(self.band_type))
        
# Constructor
    def __init__(self, imagepath, region):
        """
        Crea un RadarRegional a partir de un fichero

        imagepath -- Name of file to read.
        """

        self.imagepath = imagepath
        self.region = region        
        
                     
        self.dataset = gdal.Open(imagepath, GA_ReadOnly)
        if self.dataset is None:
            print('Unable to open %s' % imagepath)
            sys.exit(1)
        self.driver = self.dataset.GetDriver()
        self.driver.Register()
        #print 'Driver: ' + self.driver.LongName
        self.num_bands = self.dataset.RasterCount
        self.band = self.dataset.GetRasterBand(1) # Solo tiene una banda el gif
        self.band_type = self.band.DataType
        
        self.colortable = self.band.GetRasterColorTable()
        
        self.xsize = self.dataset.RasterXSize
        self.ysize = self.dataset.RasterYSize
        
        #self.projection = self.dataset.GetProjection()
        self.projection = Radar.DEFAULT_PROJ
        self.geotransform = self.dataset.GetGeoTransform()
        self.ulx = self.geotransform[0]
        self.uly = self.geotransform[3]
        self.pixelWidth = self.geotransform[1]
        self.pixelHeight = self.geotransform[5]
        self.lrx = self.ulx + self.geotransform[1] * self.xsize
        self.lry = self.uly + self.geotransform[5] * self.ysize
        #self.data = self.band.ReadAsArray(xOffset, yOffset, 1, 1)
        self.fillData(self.band)

        
        #Blocksizes
        #blockSizes = GetBlockSize(self.band)
        #xBlockSize = blockSizes[0]
        #yBlockSize = blockSizes[1]
        #print yBlockSize, xBlockSize




    def getValidColors(self):
        print self.colortable

if __name__ == '__main__':
    from Retriever import Retriever
    retriever = Retriever()
    image_dict = retriever.downloadImages(['ma'])
    for i in image_dict.iterkeys():
        radar = Regional(image_dict[i],i)
        print "Creado radar regional: " + radar.imagepath + ' Region: ' + radar.region
        radar.printReport()
        
        
        
        