#!/usr/bin/env python
from datetime import datetime,timedelta
import urllib2
import os


def roundMinutes():
    # Redondeo del minuto
    timestamp = datetime.utcnow()
    m = timestamp.minute
    m = m / 10 * 10
    timestamp = timestamp.replace(minute=m)
    d = timedelta(minutes=30)
    timestamp = timestamp - d
    return timestamp



def main():
    _regions = ['co', 'sa', 'ss', 'vd', 'za', 'ba', 'ma', 'cc', 'va', 'mu', 'se', 'ml', 'am', 'pm', 'ca']
    _url = 'http://www.aemet.es/imagenes_d/eltiempo/observacion/radar/'
    _dest = '/home/fabio/radar/img'
    timestamp = roundMinutes()
# Creacion del timestamp en la url
    for i in _regions:
        # Creamos la url para la region
        filename = timestamp.strftime("%Y%m%d%H%M") + '_r8' + i + '.gif'
        url = _url + filename
        try:
            imgData = urllib2.urlopen(url).read()
            output = open(os.path.join(_dest, filename), 'wb')
            output.write(imgData)
            output.close()
            print str(datetime.now()) + " Exito bajando " + url
        except:
            print str(datetime.now()) + " Error bajando " + url

if __name__ == '__main__':
    main()
