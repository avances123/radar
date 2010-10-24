'''
Created on 24/10/2010

@author: fabio
'''
import unittest
import radar_retriever
from urllib2 import URLError


class Test(unittest.TestCase):


    def testDescarga10minMadrid(self):
        _url = 'http://www.aemet.es/imagenes_d/eltiempo/observacion/radar/'
        url = _url + radar_retriever.getTimeStamp(10) + '_r8' + 'ma' + '.gif'
        try:
            radar_retriever.getImage(url)
        except URLError,e:
            self.fail('Codigo ' + str(e.code) + ': ' + url)
            
    def testDescarga20minMadrid(self):
        _url = 'http://www.aemet.es/imagenes_d/eltiempo/observacion/radar/'
        url = _url + radar_retriever.getTimeStamp(10) + '_r8' + 'ma' + '.gif'
        try:
            radar_retriever.getImage(url)
        except URLError,e:
            self.fail('Codigo ' + str(e.code) + ': ' + url)
            
    def testDescarga20minValencia(self):
        _url = 'http://www.aemet.es/imagenes_d/eltiempo/observacion/radar/'
        url = _url + radar_retriever.getTimeStamp(20) + '_r8' + 'va' + '.gif'
        try:
            radar_retriever.getImage(url)
        except URLError,e:
            self.fail('Codigo ' + str(e.code) + ': ' + url)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
