'''
Created on 24/10/2010

@author: fabio
'''

from osgeo import gdal, gdalconst


class RadarRegional(object):

    # Constructor
    def __init__(self, image):
        self.__image = image


    def get_image(self):
        return self.__image


    def set_image(self, value):
        self.__image = value


    def del_image(self):
        del self.__image

    image = property(get_image, set_image, del_image, "Objeto imagen de este radar")

if __name__ == '__main__':
    pass