#!/usr/bin/env python2
from datetime import datetime,timedelta
from urllib2 import URLError
import urllib2
import os,subprocess

REGIONS = ['co', 'sa', 'ss', 'vd', 'za', 'ba', 'ma', 'cc', 'va', 'mu', 'se', 'ml', 'am', 'pm', 'ca']
BASEURL = 'http://www.aemet.es/imagenes_d/eltiempo/observacion/radar/'
IMG_DIR = '/home/fabio/radar/img'
WLD_DIR = '/home/fabio/workspace/radar/wld'
DEFAULT_DELAY=10


class Retriever():
    

    def __init__(self,baseurl = BASEURL,regions = REGIONS):
        self.baseurl = baseurl
        self.regions = regions 

    
    def __getTimeStamp(self,delay = DEFAULT_DELAY):
        timestamp = datetime.utcnow()
        m = timestamp.minute
        m = m / 10 * 10
        timestamp = timestamp.replace(minute=m)
        d = timedelta(minutes=delay)
        timestamp = timestamp - d
        return timestamp.strftime("%Y%m%d%H%M")
    
    def __linkWldToGif(self,image_list):
        
        for i in image_list:
            imgpath = i[0]
            region = i[1]
            origwld_path = os.path.join(WLD_DIR, 'r3-' + region +'.wld')
            currentwld_path = imgpath.replace('.gif','.wld') 
            try:
                #retcode = subprocess.call(["ln", "-s", origwld_path, currentwld_path])
                subprocess.call(["ln", "-sf", origwld_path, currentwld_path])
            except:
                raise
    
    
    def downloadImages(self, regions = REGIONS):
 
        image_list = []
        
        print "Descargando imagenes"
        for i in regions:
            filename = self.__getTimeStamp() + '_r8' + i + '.gif'
            url = self.baseurl + filename
            path = os.path.join(IMG_DIR, filename)
            try:
                rawdata = urllib2.urlopen(url).read()
            except URLError,e:
                # Aqui viene el 404 Handler
                print "Fallo al bajar: " + url + ' Codigo: ' + str(e.code)
                continue
            try:
                output = open(path, 'wb')
                output.write(rawdata)
                output.close()
                image_list.append([path,i])
                print url + '  ->  ' + path
            except:
                pass
            
        self.__linkWldToGif(image_list)
            
        return image_list


if __name__ == '__main__':
    retriever = Retriever()
    image_list = retriever.downloadImages(['ma'])
    for i in image_list:
        print i
    
