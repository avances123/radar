'''
Created on 24/10/2010

@author: fabio
'''
from unittest import TestCase
from retriever import Retriever
from urllib2 import URLError


class Test(TestCase):
    """
     # PyUML: Do not remove this line! # XMI_ID:_210sYd-SEd-zi40xmVL8zg
    """


    def testDescarga10minMadrid(self):
        retriever = Retriever()
        url = retriever.baseurl + retriever.getTimeStamp(10) + '_r8' + 'ma' + '.gif'
        try:
            retriever.getRawImage(url)
        except URLError,e:
            self.fail('Codigo ' + str(e.code) + ': ' + url)
            
    def testDescarga20minMadrid(self):
        retriever = Retriever()
        url = retriever.baseurl + retriever.getTimeStamp(10) + '_r8' + 'ma' + '.gif'
        try:
            retriever.getRawImage(url)
        except URLError,e:
            self.fail('Codigo ' + str(e.code) + ': ' + url)
            
    def testDescarga20minValencia(self):
        retriever = Retriever()
        url = retriever.baseurl + retriever.getTimeStamp(20) + '_r8' + 'va' + '.gif'
        try:
            retriever.getRawImage(url)
        except URLError,e:
            self.fail('Codigo ' + str(e.code) + ': ' + url)
        
    def testGrabaImagenEnTmp(self):
        retriever = Retriever()
        filename = retriever.getTimeStamp(20) + '_r8' + 'ma' + '.gif'
        url = retriever.baseurl + filename
        try:
            retriever.saveImage(retriever.getRawImage(url),folder = '/tmp/')
        except Exception,e:
            self.fail(e)
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    import unittest
    unittest.main()
