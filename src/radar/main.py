'''
Created on 24/10/2010

@author: fabio
'''
from compositor import compositor
from scraper import retriever

if __name__ == '__main__':

    ret = retriever.Retriever()
    list_image = ret.getListOfImages()
    list_radars = []
    for i in list_image:
        radar = compositor.RadarRegional(i)
        list_radars.append(radar)
        