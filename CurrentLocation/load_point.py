###  STDM Code Test ###
#  authored by Joseph Kariuki
# this script creates a point shapefile and loads it into QGIS Map Interface

# importing datetime library
import sys
from qgis.core import *
from PyQt4.QtCore import *
import datetime

# getting current date and assigning it value myDate
myDate = datetime.datetime.now().date()

# creating a point with date field and loading it into memory
vectorLyr = QgsVectorLayer('Point?crs=epsg:4326&field=date', 'Current Location', 'memory')

# validating the layer and raise an exception if layer doesen't exist
if not vectorLyr.isValid():
  raise IOError, "Failed to open the layer"

# accessing dataprovider for our layer
vprv = vectorLyr.dataProvider()

# creating our new point with defined coordinates
pnt = QgsGeometry.fromPoint(QgsPoint(36.5, -0.43))

# creating new feature object
f = QgsFeature()

# setting geometry for our point
f.setGeometry(pnt)


vprv.addFeatures([f])

# updating layer extents 
vectorLyr.updateExtents()

# visualizing our layer
QgsMapLayerRegistry.instance().addMapLayer(vectorLyr)

# saving our project in home folder (Linux)
fproj = QFileInfo("/home/hempire/currentlocation.qgs")

# accessing the project instance
p = QgsProject.instance()

# saving the project file in the defined location
p.write(fproj)
### End of code 