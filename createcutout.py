"""
The following code creates a 4"x4" cutout of the F125W Band of UDS field of HST, around the coordinates given by (RA,DEC)

"""
import sys
from astropy.nddata import Cutout2D
from astropy import units as u
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord


image_file=sys.argv[1]
RA=sys.argv[2]
DEC=sys.argv[3]

f=fits.open(image_file)
w= WCS(f[0].header)
data=fits.getdata(image_file,ext=0)

sky=SkyCoord(RA, DEC, unit="deg")
position=w.world_to_pixel(sky)
size=u.Quantity((4,4),u.arcsec)
cutout=Cutout2D(data,position,size,wcs=w)

hdu=fits.PrimaryHDU()
hdu.data=cutout.data
hdu.header=f[0].header
hdu.header.update(cutout.wcs.to_header())
outputcutout=image_file[0:5]+'2.fits'
hdu.writeto(outputcutout,overwrite=True)
