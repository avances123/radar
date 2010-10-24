#!/usr/bin/env python
from datetime import datetime,timedelta
import urllib2
import os
from urllib2 import URLError


def getTimeStamp(delay=30):
    # Redondeo del minuto
    timestamp = datetime.utcnow()
    m = timestamp.minute
    m = m / 10 * 10
    timestamp = timestamp.replace(minute=m)
    d = timedelta(minutes=delay)
    timestamp = timestamp - d
    return timestamp.strftime("%Y%m%d%H%M")

def getImage(url):
    try:
        imgData = urllib2.urlopen(url).read()
    except URLError:
        raise
    return imgData

def saveImage(stream,filename,folder):
    try:
        output = open(os.path.join(folder, filename), 'wb')
        output.write(stream)
        output.close()
    except:
        pass
    

def main():
    _regions = ['co', 'sa', 'ss', 'vd', 'za', 'ba', 'ma', 'cc', 'va', 'mu', 'se', 'ml', 'am', 'pm', 'ca']
    _url = 'http://www.aemet.es/imagenes_d/eltiempo/observacion/radar/'
    _dest = '/home/fabio/radar/img'
# Creacion del timestamp en la url
    for i in _regions:
        # Creamos la url para la region
        filename = getTimeStamp() + '_r8' + i + '.gif'
        url = _url + filename
        try:
            imgData = getImage(url)
            saveImage(imgData, filename, _dest)
            print str(datetime.now()) + " Exito bajando " + url
        except Exception:
            print str(datetime.now()) + " Error bajando " + url

if __name__ == '__main__':
    main()
