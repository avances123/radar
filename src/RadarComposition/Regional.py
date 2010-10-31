#!/usr/bin/env python
'''
Created on 26/10/2010

@author: fabio
'''
from Radar import Radar


class Regional(Radar):  # Hereda de Radar
    '''
    classdocs
    '''

    def __init__(self,imagepath,region):
        '''
        Constructor
        '''
        #super(Regional, self ).__init__()
        self.imagepath = imagepath
        self.region = region

    def getValidColors(self):
        pass

if __name__ == '__main__':
    from Retriever import Retriever
    retriever = Retriever()
    image_dict = retriever.downloadImages(['ma'])
    for i in image_dict.iterkeys():
        radar = Regional(image_dict[i],i)
        print "Creado radar regional: " + radar.imagepath + '  ' + radar.region
        
        
        
        