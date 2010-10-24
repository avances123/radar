'''
Created on 24/10/2010

@author: fabio
'''

from osgeo import gdal, gdal_array
from osgeo.gdalconst import GA_ReadOnly
import numpy



class RadarRegional(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_H49OgN-ZEd-4cbf1aHA2Wg
    """

    # Image Property
    def get_imagepath(self):
        return self.__imagepath
    def set_imagepath(self, value):
        self.__imagepath = value
    def del_imagepath(self):
        del self.__imagepath
    def get_rows(self):
        return self.__rows
    def get_cols(self):
        return self.__cols
    def set_rows(self, value):
        self.__rows = value
    def set_cols(self, value):
        self.__cols = value
    def del_rows(self):
        del self.__rows
    def del_cols(self):
        del self.__cols
    image = property(get_imagepath, set_imagepath, del_imagepath, "Objeto imagen de este radar")
    rows = property(get_rows, set_rows, del_rows, "Number of rows of this dataset")
    cols = property(get_cols, set_cols, del_cols, "Number of cols of this dataset")
    



    
    # Constructor
    def __init__(self, imagepath):
        self.__imagepath = imagepath
        self.dataset = self.getDataSet(imagepath)
        self.rows = self.dataset.RasterYSize
        self.cols = self.dataset.RasterXSize
        self.bands = self.dataset.RasterCount
        
        
    
    # TODO Poner mas control
    def getDataSet(self,path):
        gdal.AllRegister()
        try:
            ds = gdal.Open(path, GA_ReadOnly)
            if ds is None:
                raise Exception
        except:
            print 'Error obteniendo dataset en la imagen: ' + path
        return ds
    

    def getDataAsArray(self,path):
        try:
            dataset = self.getDataSet(path)
            band = dataset.GetRasterBand(1)
            #scanline = inband.ReadAsArray(0, i, inband.XSize, 1, inband.XSize, 1)
            #def ReadAsArray(self, xoff=0, yoff=0, win_xsize=None, win_ysize=None,buf_xsize=None, buf_ysize=None, buf_obj=None):
            data = band.ReadAsArray(0, 0, band.XSize, 1, band.XSize, 1)
            #data = None
        except:
            pass
        return data

if __name__ == '__main__':
    pass

