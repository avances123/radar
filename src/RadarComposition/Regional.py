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
    
import numpy

import subprocess,sys
from Radar import Radar


class Regional(Radar):  # Hereda de Radar
    '''
    classdocs
    '''
    NoData = 127
    colores = {(  0,  0,  0,255):0,\
               (  0,  0,252,255):15,\
               (  0,148,252,255):21,\
               (  0,252,252,255):27,\
               ( 67,131, 35,255):33,\
               (  0,192,  0,255):39,\
               (  0,255,  0,255):45,\
               (255,255,  0,255):51,\
               (255,187,  0,255):57,\
               (255,127,  0,255):63,\
               (255,  0,  0,255):69,\
               (200,  0, 90,255):75} 

    def __fillArrayData(self,band):
        self.data = band.ReadAsArray(0,0,self.xsize,self.ysize)
        #self.band = None # Ahorro de memoria
        print self.data #(math matrix notation is [row,col], not [x,y])
    
    
    def __getValidColors(self):
 
        #for i in range(min(256,self.colortable.GetCount())):
        valid_gifindexes = {}
        for i in range(self.colortable.GetCount()):
            entry = self.colortable.GetColorEntry(i)
            if self.colores.has_key(entry):
                valid_gifindexes[i] = self.colores[entry]
        return valid_gifindexes    
    
    
    
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
        
                     
        #self.dataset = gdal.Open(imagepath, GA_ReadOnly)
        self.dataset = gdal.Open(imagepath)
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
        self.projection = Radar.DEFAULT_PROJ_WKT
        self.geotransform = self.dataset.GetGeoTransform()
        self.ulx = self.geotransform[0]
        self.uly = self.geotransform[3]
        self.pixelWidth = self.geotransform[1]
        self.pixelHeight = self.geotransform[5]
        self.lrx = self.ulx + self.geotransform[1] * self.xsize
        self.lry = self.uly + self.geotransform[5] * self.ysize
        #self.data = self.band.ReadAsArray(xOffset, yOffset, 1, 1)
        self.__fillArrayData(self.band)
        self.valid_gifindexes = self.__getValidColors()
        
        #gdal.ReprojectImage(self.dataset,self.dataset,self.DEFAULT_PROJ_WKT,self.LATLONG_PROJ)




            
            
            
    def swapValues(self,data): # TODO debe ser tipo gdalnumeric, numpy array
        '''
        Cambia los valores de un array de etrada seguin el mapping de valid_gifindexes
        '''
        
        for i in range(len(data)):
            for j in range (len(data[0])):
                if data[i,j] in  self.valid_gifindexes:
                    # TODO aqui se pilla el pixel valido, cambiar de valor por el valor meteologica
                    #print "Es un pixel valido: " + str(i) + ',' + str(j)
                    pass
                else:
                    #print "Es un pixel basura: " + str(i) + ',' + str(j)
                    data[i,j] = self.NoData

        #data = numpy.where(data in self.valid_gifindexes.all(),self.NoData,data) # Si no es un color valido, no data
        return data






  
    def dumpToGeoTiff(self,newfile):
        """
        Graba en un GeoTiff el radar regional
        
        newfile es el path donde se escribira el GeoTiff
        """
        # create the output image
        driver = gdal.GetDriverByName("GTiff")
        dsOut = driver.Create('out.tiff', self.xsize, self.ysize, 1, self.band.DataType)
        bandOut = dsOut.GetRasterBand(1)
        #self.data = self.band.ReadAsArray(0,0,self.xsize, self.ysize)
        bandOut.WriteArray(self.data, 0,0)
        bandOut.SetNoDataValue(self.NoData)

        
        # compute statistics for the output
        bandOut.FlushCache()
        stats = bandOut.GetStatistics(0, 1)
        print stats

        # set the geotransform and projection on the output
        #geotransform = [minX, pixelWidth1, 0, maxY, 0, pixelHeight1]
        geotransform = [self.ulx, self.pixelWidth, 0, self.uly, 0, self.pixelHeight]
        dsOut.SetGeoTransform(geotransform)
        dsOut.SetProjection(self.projection)
        '''
        ReprojectImage(Dataset src_ds, Dataset dst_ds, char src_wkt = None, 
        char dst_wkt = None, GDALResampleAlg eResampleAlg = GRA_NearestNeighbour, 
        double WarpMemoryLimit = 0.0, 
        double maxerror = 0.0, GDALProgressFunc callback = None, 
        void callback_data = None) -> CPLErr
        '''
        #gdal.ReprojectImage(self.dataset,self.dataset,self.DEFAULT_PROJ,self.LATLONG_PROJ)
        #subprocess.call(["gdalwarp","-t_srs","+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs","out.tiff","out1.tiff"])
        #subprocess.call("gdalwarp","-t_srs \"+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs\" out.tiff out1.tiff")

        
if __name__ == '__main__':
    from Retriever import Retriever
    retriever = Retriever()
    image_dict = retriever.downloadImages(['ba'])
    for i in image_dict.iterkeys():
        radar = Regional(image_dict[i],i) #(imagepath, region)
        #print "Creado radar regional: " + radar.imagepath + ' Region: ' + radar.region
        radar.printReport()
        #valid_gifindexes = radar.__getValidColors()
        radar.data = radar.swapValues(radar.data)
        radar.dumpToGeoTiff('out.tiff')
        
        
        
        
