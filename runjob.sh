#!/bin/bash

ID=${1}
RA=${4}
DEC=${5}
python3 createcutout.py F125W.fits ${RA} ${DEC}
python3 createcutout.py F140W.fits ${RA} ${DEC}
python3 createcutout.py F814W.fits  ${RA} ${DEC}
python3 colourimg.py ${ID}
