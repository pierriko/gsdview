### Copyright (C) 2008 Antonio Valentino <a_valentino@users.sf.net>

### This file is part of GSDView.

### GSDView is free software; you can redistribute it and/or modify
### it under the terms of the GNU General Public License as published by
### the Free Software Foundation; either version 2 of the License, or
### (at your option) any later version.

### GSDView is distributed in the hope that it will be useful,
### but WITHOUT ANY WARRANTY; without even the implied warranty of
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
### GNU General Public License for more details.

### You should have received a copy of the GNU General Public License
### along with GSDView; if not, write to the Free Software
### Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA.

'''Package info.'''

__author__   = 'Antonio Valentino <a_valentino@users.sf.net>'
__date__     = '$Date$'
__revision__ = '$Revision$'
__version__  = (0,3,0)

__all__ = ['name', 'version', 'short_description', 'description',
           'author', 'author_email', 'copyright', 'license_type',
           'website', 'website_label']

import sys

name = 'GSDView'
version = '.'.join(map(str, __version__)) + 'a'

short_description = 'Geo-Spatial Data Viewer'
description = '''GSDView (Geo-Spatial Data Viewer) is a lightweight
viewer for geo-spatial data and products.
It is written in python and Qt4 and it is mainly intended to be a graphical
frotend for the GDAL library and tools.
GSDView is modular and has a simple plug-in architecture.

'''

author = 'Antonio Valentino'
author_email = 'a_valentino@users.sf.net'
copyright = 'Copytight (C) 2008 %s <%s>' % (author, author_email)
#license = _get_license()
license_type = 'GNU GPL'
website = 'http://gsdview.sourceforge.net'
website_label = website

#artists = None
#documenters = ('AV',)
#thanks = None
#translator_credits = None

# @TODO: check (too many imports)
from PyQt4 import QtCore
import numpy
try:
    from osgeo import gdal
except ImportError:
    import gdal

all_versions = [
    ('GSDView', version, website),
    ('Python', '.'.join(map(str,sys.version_info[:3])), 'www.python.org'),
    ('PyQt4', QtCore.PYQT_VERSION_STR, 'http://www.riverbankcomputing.co.uk/pyqt'),
    ('Qt', QtCore.QT_VERSION_STR, 'http://www.trolltech.com/qt'),
    ('numpy', numpy.version.version, 'http://www.scipy.org'),
]

try:
    gdalversion = gdal.VersionInfo('RELEASE_NAME')
except AttributeError:
    gdalversion = 'Unknown'
all_versions.append(('GDAL', gdalversion, 'http://www.gdal.org'))

all_versions_str = '\n'.join('%s v. %s, (%s)' % (sw, version_, link)
                                        for sw, version_, link in all_versions)

if __name__ == '__main__':
    print 'name',name
    print 'version:', version
    print 'short_description:', short_description
    print 'description:', description
    print 'author:', author
    print 'author_email:', author_email
    print 'copyright:', '\n'.join(copyright)
    print 'license_type:', license_type
    print 'website:', website
    print 'website_label:', website_label
    print 'all_versions_str:', all_versions_str