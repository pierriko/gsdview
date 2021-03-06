# -*- coding: utf-8 -*-

### Copyright (C) 2008-2012 Antonio Valentino <a_valentino@users.sf.net>

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


import sys
import platform

import numpy as np

import qt
from qt import QtCore


__author__ = 'Antonio Valentino <a_valentino@users.sf.net>'
__date__ = '$Date$'
__revision__ = '$Revision$'
__version__ = (0, 7, 0)

__all__ = ['name', 'version', 'short_description', 'description',
           'author', 'author_email', 'copyright', 'license_type',
           'website', 'website_label', 'all_versions', 'all_versions_str']

name = 'GSDView'
version = '.'.join(str(v) for v in __version__) + '.dev'

short_description = 'Geo-Spatial Data Viewer Open Source Edition'
description = '''GSDView (Geo-Spatial Data Viewer) is a lightweight
viewer for geo-spatial data and products.

It is written in python and Qt4 and it is mainly intended to be a graphical
frotend for the GDAL library and tools.

GSDView is modular and has a simple plug-in architecture.

'''

author = 'Antonio Valentino'
author_email = 'a_valentino@users.sf.net'
copyright = 'Copyright (C) 2008-2012 %s <%s>' % (author, author_email)
#license = _get_license()
license_type = 'GNU GPL'
website = 'http://gsdview.sourceforge.net'
website_label = website
download_url = 'http://sourceforge.net/projects/gsdview/files'


all_versions = [
    ('GSDView', version, website),
    ('Python', '.'.join(map(str, sys.version_info[:3])), 'www.python.org'),
    ('Qt', QtCore.qVersion(), 'http://qt.nokia.com'),
    ('numpy', np.version.version, 'http://www.scipy.org'),
]

if qt.qt_api == 'pyqt':
    import sip
    all_versions.append(('sip', sip.SIP_VERSION_STR,
                         'http://www.riverbankcomputing.co.uk/software/sip'))
    all_versions.append(('PyQt4', QtCore.PYQT_VERSION_STR,
                         'http://www.riverbankcomputing.co.uk/software/pyqt'))
    try:
        from PyQt4 import Qsci
    except ImportError:
        pass
    else:
        all_versions.append(('QScintilla', Qsci.QSCINTILLA_VERSION_STR,
                'http://www.riverbankcomputing.co.uk/software/qscintilla'))

elif qt.qt_api == 'pyside':
    import PySide
    all_versions.append(
        ('PySide', PySide.__version__, 'http://www.pyside.org'))

if platform.dist() != ('', '', ''):
    all_versions.append(('GNU/Linux', ' '.join(platform.dist()), ''))
elif platform.mac_ver() != ('', ('', '', ''), ''):
    all_versions.append(('Mac OS X', platform.mac_ver()[0],
                         'http://www.apple.com/macosx'))
elif platform.win32_ver() != ('', '', '', ''):
    all_versions.append(('Windows', platform.win32_ver()[0],
                         'http://www.microsoft.com/windows'))


def all_versions_str():
    return '\n'.join(
        '%s v. %s %s' % (sw, version_, '(%s)' % link if link else '')
                                    for sw, version_, link in all_versions)
