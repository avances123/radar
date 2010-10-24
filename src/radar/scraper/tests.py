'''
Created on 24/10/2010

@author: fabio
'''
import unittest
from retriever import Retriever
from urllib2 import URLError


class Test(unittest.TestCase):


    def testDescarga10minMadrid(self):
        retriever = Retriever()
        url = retriever.baseurl + retriever.getTimeStamp(10) + '_r8' + 'ma' + '.gif'
        try:
            retriever.getImage(url)
        except URLError,e:
            self.fail('Codigo ' + str(e.code) + ': ' + url)
            
    def testDescarga20minMadrid(self):
        retriever = Retriever()
        url = retriever.baseurl + retriever.getTimeStamp(10) + '_r8' + 'ma' + '.gif'
        try:
            retriever.getImage(url)
        except URLError,e:
            self.fail('Codigo ' + str(e.code) + ': ' + url)
            
    def testDescarga20minValencia(self):
        retriever = Retriever()
        url = retriever.baseurl + retriever.getTimeStamp(20) + '_r8' + 'va' + '.gif'
        try:
            retriever.getImage(url)
        except URLError,e:
            self.fail('Codigo ' + str(e.code) + ': ' + url)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
