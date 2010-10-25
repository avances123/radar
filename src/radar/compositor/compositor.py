'''
Created on 24/10/2010

@author: fabio
'''

from osgeo import gdal
import sys,subprocess
import re

WLD_DIR = '/home/fabio/workspace/radar/wld/'

class RadarRegional(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_H49OgN-ZEd-4cbf1aHA2Wg
    """

    
    # Constructor
    def __init__(self, filename):
        """
        Crea un RadarRegional a partir de un fichero

        filename -- Name of file to read.
        """
        
        
        retcode = subprocess.call(["ln", "-s"])
              
        self.dataset = gdal.Open(filename)
        if self.dataset is None:
            print('Unable to open %s' % filename)
            sys.exit(1)

        self.filename = filename
        self.num_bands = self.dataset.RasterCount
        self.band = self.dataset.GetRasterBand(1) # Solo tiene una banda el gif
        self.colortable = self.band.GetRasterColorTable()
        self.xsize = self.dataset.RasterXSize
        self.ysize = self.dataset.RasterYSize
        self.band_type = self.band.DataType
        self.projection = self.dataset.GetProjection()
        self.geotransform = self.dataset.GetGeoTransform()
        self.ulx = self.geotransform[0]
        self.uly = self.geotransform[3]
        self.lrx = self.ulx + self.geotransform[1] * self.xsize
        self.lry = self.uly + self.geotransform[5] * self.ysize



    def report(self):
        print('Filename: '+ self.filename)
        print('File Size: %dx%dx%d' % (self.xsize, self.ysize, self.num_bands))
        print('Pixel Size: %f x %f' % (self.geotransform[1],self.geotransform[5]))
        print('UL:(%f,%f)   LR:(%f,%f)'  % (self.ulx,self.uly,self.lrx,self.lry))
        
    def dumpToGeoTiff(self,newfile):
        """
        Graba en un GeoTiff el radar regional
        
        newfile es el path donde se escribira el GeoTiff
        """
        # Callback para el proceso
        def progress_cb( complete, message, cb_data ):
            print('%s %d' % (cb_data, complete))
            
        geotiff = gdal.GetDriverByName("GTiff")
        if geotiff is None:
            print('GeoTIFF driver not registered.')
            sys.exit(1)
        print('Importing to Tiled GeoTIFF file: %s' % newfile)
        new_dataset = geotiff.CreateCopy( newfile, self.dataset, 0,
                                  ['TILED=YES',], #Copiado, no se lo que hace
                                  callback = progress_cb, #Estudiar esto
                                  callback_data = '' )  #Estudiar esto


if __name__ == '__main__':
    pass

