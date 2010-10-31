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
    image_list = retriever.downloadImages(['ma'])
    for i in image_list:
        radar = Regional(i[0],i[1]) # Hay que cambiar a diccionario    
        print "Creado radar regional: " + radar.imagepath + '  ' + radar.region
        
        
        
        