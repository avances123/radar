'''
Created on 24/10/2010

@author: fabio

adfGeoTransform[0] /* top left x */
adfGeoTransform[1] /* w-e pixel resolution */
adfGeoTransform[2] /* rotation, 0 if image is "north up" */
adfGeoTransform[3] /* top left y */
adfGeoTransform[4] /* rotation, 0 if image is "north up" */
adfGeoTransform[5] /* n-s pixel resolution */
'''

from osgeo import gdal
import sys



class RadarRegional(object):

    """
     # PyUML: Do not remove this line! # XMI_ID:_H49OgN-ZEd-4cbf1aHA2Wg
    """

    DEFAULT_PROJ = "+proj=lcc +lat_1=46.5 +lat_2=33.5 +lat_0=0 +lon_0=0 +x_0=0 +y_0=0 +ellps=GRS80 +units=m +no_defs"
    LATLONG_PROJ = "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs "
    
    # Constructor
    def __init__(self, filename, region):
        """
        Crea un RadarRegional a partir de un fichero

        filename -- Name of file to read.
        """

        self.filename = filename
        self.region = region        
        
                     
        self.dataset = gdal.Open(filename)
        if self.dataset is None:
            print('Unable to open %s' % filename)
            sys.exit(1)
        self.driver = self.dataset.GetDriver()
        print 'Driver: ' + self.driver.LongName
        self.num_bands = self.dataset.RasterCount
        self.band = self.dataset.GetRasterBand(1) # Solo tiene una banda el gif
        self.colortable = self.band.GetRasterColorTable()
        self.xsize = self.dataset.RasterXSize
        self.ysize = self.dataset.RasterYSize
        self.band_type = self.band.DataType
        #self.projection = self.dataset.GetProjection()
        self.projection = RadarRegional.DEFAULT_PROJ
        self.geotransform = self.dataset.GetGeoTransform()
        self.ulx = self.geotransform[0]
        self.uly = self.geotransform[3]
        self.lrx = self.ulx + self.geotransform[1] * self.xsize
        self.lry = self.uly + self.geotransform[5] * self.ysize

    def reprojection(self):
        """
        gdalwarp -s_srs '+proj=lcc +lat_1=46.5 +lat_2=33.5 +lat_0=0 +lon_0=0 +x_0=0 +y_0=0 +ellps=GRS80 +units=m +no_defs ' -t_srs '+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs ' 201010251510_r8za.gif 201010251510_r8za.tiff
        def CreateAndReprojectImage( src_ds, dst_filename, src_wkt = None, dst_wkt = None,
                                        dst_driver = None, create_options = [],
                                        eResampleAlg = GRA_NearestNeighbour,
                                        warp_memory = 0.0, maxerror = 0.0 ):
        gdal.CreateAndReprojectImage(self.dataset,'reprojected.tif',self.DEFAULT_PROJ,self.LATLONG_PROJ)
        """
       
        pass

    def report(self):
        print('Filename: '+ self.filename)
        print('File Size: %dx%dx%d' % (self.xsize, self.ysize, self.num_bands))
        print('Pixel Size: %f x %f' % (self.geotransform[1],self.geotransform[5]))
        print('UL:(%f,%f)   LR:(%f,%f)'  % (self.ulx,self.uly,self.lrx,self.lry))
        print('Projection '  + self.projection)
        print('Band Type: '  + str(self.band_type))
        
    def dumpToGeoTiff(self,newfile):
        """
        Graba en un GeoTiff el radar regional
        
        newfile es el path donde se escribira el GeoTiff
        """
        # Callback para el proceso
        def progress_cb( complete, message, cb_data ):
            #print('%s %d' % (cb_data, complete))
            pass
        
        geotiff = gdal.GetDriverByName("GTiff")
        if geotiff is None:
            print('GeoTIFF driver not registered.')
            sys.exit(1)
        print('Importing to Tiled GeoTIFF file: %s' % newfile)
        new_dataset = geotiff.CreateCopy( newfile, self.dataset, 0,
                                  ['TILED=YES',], #Copiado, no se lo que hace
                                  callback = progress_cb, #Estudiar esto
                                  callback_data = '' )  #Estudiar esto


if __name__ == '__main__':
    pass

