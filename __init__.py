# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CurrentLocation
                                 A QGIS plugin
 Plugin for creating a shapefile using single click
                             -------------------
        begin                : 2018-10-09
        copyright            : (C) 2018 by Joseph Kariuki
        email                : joehene@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CurrentLocation class from file CurrentLocation.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .current_location import CurrentLocation
    return CurrentLocation(iface)
