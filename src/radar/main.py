'''
Created on 24/10/2010

@author: fabio
'''
from compositor import compositor
from scraper import retriever


if __name__ == '__main__':

    ret = retriever.Retriever()
    list_image = ret.getListOfImages(['ma'])
    list_radars = []
    for i in list_image:
        radar = compositor.RadarRegional(i)
        data = radar.getDataAsArray(i)
        print data
        list_radars.append(radar)
        print "Imagen " + radar.image + "  (" + str(radar.rows) + "," + str(radar.cols) + ")"
        print "Imagen " + radar.image + "  Numero de bandas: "+ str(radar.bands)