"""
The following piece of code combines 7"x7" cutout data from three cutouts from the F125W,F140W,F814W Bands of HST
and creates a composite image 
"""
#! usr/bin/python3
import aplpy 
import sys


ID=sys.argv[1]
outputimg =ID+".jpeg"

aplpy.make_rgb_cube(['F125W2.fits','F140W2.fits','F814W2.fits'],'cube.fits')
aplpy.make_rgb_image('cube.fits', 'cube.jpeg')
img = aplpy.FITSFigure('cube_2d.fits')
img.show_rgb('cube.jpeg')
img.add_label(0.1,0.9, 'Imsize=7"x7"',color='yellow', relative=True)
img.add_label(0.9,0.9, ID,color='yellow',size=11, relative=True)
img.save(outputimg)
