#!/usr/bin/env python2
from datetime import datetime,timedelta
from urllib2 import URLError
import urllib2
import os


class Retriever():

    def __init__(self,
                 baseurl = 'http://www.aemet.es/imagenes_d/eltiempo/observacion/radar/',
                 regions = ['co', 'sa', 'ss', 'vd', 'za', 'ba', 'ma', 'cc', 'va', 'mu', 'se', 'ml', 'am', 'pm', 'ca']
                 ):
        self.baseurl = baseurl
        self.regions = regions 

    
    def getTimeStamp(self,delay=30):
        timestamp = datetime.utcnow()
        m = timestamp.minute
        m = m / 10 * 10
        timestamp = timestamp.replace(minute=m)
        d = timedelta(minutes=delay)
        timestamp = timestamp - d
        return timestamp.strftime("%Y%m%d%H%M")
    
    def getRawImage(self,url):
        try:
            imgData = urllib2.urlopen(url).read()
        except URLError:
            raise
        return imgData
    
    
    def saveImage(self,stream,filename = 'test.gif',folder = '/home/fabio/radar/img'):
        path = os.path.join(folder, filename)
        try:
            output = open(path, 'wb')
            output.write(stream)
            output.close()
        except Exception:
            raise
        return path
    
    def getListOfImages(self):
        image_list = []
        for i in self.regions:
            filename = self.getTimeStamp() + '_r8' + i + '.gif'
            url = self.baseurl + filename
            path=''
            try:
                path = self.saveImage(self.getRawImage(url),filename)
                image_list.append(path)
            except:
                pass
            
        return image_list
    

    

def main():
         
    retriever = Retriever()
    list = retriever.getListOfImages()
    for i in list:
        print i

if __name__ == '__main__':
    main()
