'''
Created on 24/10/2010

@author: fabio
'''
from compositor import compositor
from scraper import retriever




if __name__ == '__main__':

    ret = retriever.Retriever()
    list_image = ret.getListOfImages(['ma'])
    for i in list_image:
        radar = compositor.RadarRegional(i)
        #radar.report()
        radar.dumpToGeoTiff('out.tif')