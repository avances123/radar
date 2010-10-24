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
    
    def getImage(self,url):
        try:
            imgData = urllib2.urlopen(url).read()
        except URLError:
            raise
        return imgData
    
    def saveImage(self,stream,filename,folder = '/home/fabio/radar/img'):
        try:
            output = open(os.path.join(folder, filename), 'wb')
            output.write(stream)
            output.close()
        except:
            pass

    

def main():
         
    retriever = Retriever()
    for i in retriever.regions:
        filename = retriever.getTimeStamp() + '_r8' + i + '.gif'
        url = retriever.baseurl + filename
        try:
            imgData = retriever.getImage(url)
            retriever.saveImage(imgData, filename)
            print str(datetime.now()) + " Exito bajando " + url
        except Exception,e:
            print str(datetime.now()) + " Error bajando " + url + ':' + str(e.code)

if __name__ == '__main__':
    main()
