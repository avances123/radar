'''
Created on 24/10/2010

@author: fabio
'''

from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly


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
    image = property(get_imagepath, set_imagepath, del_imagepath, "Objeto imagen de este radar")
    
    # Constructor
    def __init__(self, imagepath):
        self.__imagepath = imagepath
        self.dataset = self.getDataSet(imagepath)
    
    def getDataSet(self,path):
        gdal.AllRegister()
        try:
            ds = gdal.Open(path, GA_ReadOnly)
            if ds is None:
                raise Exception
            else:
                print ds
        except:
            print 'Error obteniendo dataset en la imagen: ' + path
        return ds

if __name__ == '__main__':
    pass

