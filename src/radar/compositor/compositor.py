'''
Created on 24/10/2010

@author: fabio
'''

from osgeo import gdal
#gdal.TermProgress = gdal.TermProgress_nocb
import sys



class RadarRegional(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_H49OgN-ZEd-4cbf1aHA2Wg
    """
    # Constructor
    def __init__(self, filename):
        """
        Initialize file_info from filename

        filename -- Name of file to read.

        Returns 1 on success or 0 if the file can't be opened.
        """
        fh = gdal.Open(filename)
        if fh is None:
            print('Unable to open %s' % filename)
            sys.exit(1)

        self.dataset = fh
        self.filename = filename
        self.bands = fh.RasterCount
        self.xsize = fh.RasterXSize
        self.ysize = fh.RasterYSize
        self.band_type = fh.GetRasterBand(1).DataType
        self.projection = fh.GetProjection()
        self.geotransform = fh.GetGeoTransform()
        self.ulx = self.geotransform[0]
        self.uly = self.geotransform[3]
        self.lrx = self.ulx + self.geotransform[1] * self.xsize
        self.lry = self.uly + self.geotransform[5] * self.ysize

        ct = fh.GetRasterBand(1).GetRasterColorTable()
        if ct is not None:
            self.ct = ct.Clone()
        else:
            self.ct = None

    def report( self ):
        print('Filename: '+ self.filename)
        print('File Size: %dx%dx%d' \
              % (self.xsize, self.ysize, self.bands))
        print('Pixel Size: %f x %f' \
              % (self.geotransform[1],self.geotransform[5]))
        print('UL:(%f,%f)   LR:(%f,%f)' \
              % (self.ulx,self.uly,self.lrx,self.lry))
        
    def dumpToGeoTiff(self,newfile):
        def progress_cb( complete, message, cb_data ):
            print('%s %d' % (cb_data, complete))
        geotiff = gdal.GetDriverByName("GTiff")
        if geotiff is None:
            print('GeoTIFF driver not registered.')
            sys.exit(1)
        print('Importing to Tiled GeoTIFF file: %s' % newfile)
        new_dataset = geotiff.CreateCopy( newfile, self.dataset, 0,
                                  ['TILED=YES',],
                                  callback = progress_cb,
                                  callback_data = '' )


if __name__ == '__main__':
    pass

