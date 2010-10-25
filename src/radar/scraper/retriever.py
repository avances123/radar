#!/usr/bin/env python2
from datetime import datetime,timedelta
from urllib2 import URLError
import urllib2
import os,subprocess

REGIONS = ['co', 'sa', 'ss', 'vd', 'za', 'ba', 'ma', 'cc', 'va', 'mu', 'se', 'ml', 'am', 'pm', 'ca']
BASEURL = 'http://www.aemet.es/imagenes_d/eltiempo/observacion/radar/'
IMGDIR = '/home/fabio/radar/img'
WLDDIR = '/home/fabio/workspace/radar/wld'


class Retriever():
    """
     # PyUML: Do not remove this line! # XMI_ID:_22LRsN-SEd-zi40xmVL8zg
    """

    def __init__(self,baseurl = BASEURL,regions = REGIONS):
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
        """
        Se baja una url con urllib2 y devuelve los datos
        """
        try:
            imgData = urllib2.urlopen(url).read()
        except URLError:
            raise
        return imgData
    
    
    def saveImage(self,stream,filename = 'no_name.gif',folder = IMGDIR):
        """
        Guarda datos en bruto a una imagen
        stream = datos en bruto procedentes de self.getRawImage(url)
        filename = nombre del fichero
        folder = carpeta donde se guardara
        
        Devuelve el path absoluto de la imagen si la ha guardado con exito
        """
        path = os.path.join(folder, filename)
        try:
            output = open(path, 'wb')
            output.write(stream)
            output.close()
        except Exception:
            raise
        return path

    # Hacerlo privada
    def linkWldToGif(self,image_list):
        for i in image_list:
            imgpath = i[0]
            region = i[1]
            origwld_path = os.path.join(WLDDIR, 'r3-' + region +'.wld')
            currentwld_path = imgpath.replace('.gif','.wld') 
            try:
                #retcode = subprocess.call(["ln", "-s", origwld_path, currentwld_path])
                subprocess.call(["ln", "-s", origwld_path, currentwld_path])
            except:
                raise
            
                
    
    def getListOfImages(self,region_list = REGIONS):
        image_list = []
        for i in region_list:
            filename = self.getTimeStamp() + '_r8' + i + '.gif'
            url = self.baseurl + filename
            #path=''
            try:
                rawdata = self.getRawImage(url)
                path = self.saveImage(rawdata,filename)
                image_list.append([path,i])
                print 'Exito bajando: ' + path
            except:
                pass
        self.linkWldToGif(image_list)
        return image_list


        
    

def main():
         
    retriever = Retriever()
    list = retriever.getListOfImages()
    for i in list:
        print i

if __name__ == '__main__':
    main()
