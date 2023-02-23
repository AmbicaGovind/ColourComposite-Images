"""
The following piece of code combines 4"x4" cutout data from three cutouts from the F125W,F140W,F814W Bands of HST
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
img.add_label(0.2,0.9, 'Imsize=4"x4"',color='yellow', relative=True,size=20)
img.add_label(0.8,0.9, ID,color='yellow',relative=True,size=20)
axes=aplpy.AxisLabels(img)
axes.set_font(size=20)
axes.set_xtext('RA')
axes.set_ytext('DEC')
ticks = aplpy.TickLabels(img)
ticks.set_font(size=20)
ticks.show_x()
ticks.show_y()
img.save(outputimg)
