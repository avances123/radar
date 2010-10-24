'''
Created on 24/10/2010

@author: fabio
'''

from osgeo import gdal, gdalconst


class RadarRegional(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_H49OgN-ZEd-4cbf1aHA2Wg
    """

    # Constructor
    def __init__(self, image):
        self.__image = image
        
    # Image Property
    def get_image(self):
        return self.__image
    def set_image(self, value):
        self.__image = value
    def del_image(self):
        del self.__image
    image = property(get_image, set_image, del_image, "Objeto imagen de este radar")

if __name__ == '__main__':
    from radar.scraper.retriever import Retriever
    retriever = Retriever()
    list = retriever.getListOfImages()
    for i in list:
        print i

