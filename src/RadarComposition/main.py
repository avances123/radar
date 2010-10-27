'''
Created on 24/10/2010

@author: fabio
'''
from RadarComposition import compositor
from RadarComposition import retriever




if __name__ == '__main__':

    ret = retriever.Retriever()
    list_image = ret.getListOfImages(['ss'])
    #list_image = ret.getListOfImages()
    for i in list_image:
        radar = compositor.RadarRegional(i[0],i[1])
        radar.report()
        radar.dumpToGeoTiff('out.tif')
        radar.reprojection()
        for i in range(min(256,radar.colortable.GetCount())):
            entry = radar.colortable.GetColorEntry(i)
            #print entry