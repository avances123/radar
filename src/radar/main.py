'''
Created on 24/10/2010

@author: fabio
'''
from compositor import compositor
from scraper import retriever
import numpy

if __name__ == '__main__':

    ret = retriever.Retriever()
    list_image = ret.getListOfImages(['ma'])
    list_radars = []
    for i in list_image:
        radar = compositor.RadarRegional(i)
        data = radar.getDataAsArray(i)
        print 'Tamanio de la banda: ' + str(data.shape)
        print data
        radar.getHistogram('/home/fabio/meteologica/tiffs/predicciones500-alarmaicona-20100513-d0.tiff')
        list_radars.append(radar)