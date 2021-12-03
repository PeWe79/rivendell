#!%PYTHON_BANGPATH%

# list_groups.py
#
# rivwebpyapi test script for Rivendell
#
#  Access the 'ListGroups' call.
#
#   (C) Copyright 2021 Fred Gleason <fredg@paravelsystems.com>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License version 2 as
#   published by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public
#   License along with this program; if not, write to the Free Software
#   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#

import getpass
import rivwebpyapi
import sys

#
# Get login parameters
#
usage='list_groups --url=<rd-url> --username=<rd-username> [--password=<passwd>]'
url='';
username=''
password=''
trackable=False
for arg in sys.argv:
    f0=arg.split('=')
    if(len(f0)==2):
        if(f0[0]=='--url'):
            url=f0[1]
        if(f0[0]=='--username'):
            username=f0[1]
        if(f0[0]=='--password'):
            password=f0[1]
if(not password):
    password=getpass.getpass()
if((not url)or(not username)):
    print(usage)
    sys.exit(1)

#
# Get the group list
#
webapi=rivwebpyapi.rivwebpyapi(url=url,username=username,password=password)
groups=webapi.ListGroups()

#
# Display the group list
#
for grp in groups:
    print('name: '+grp['name'])
    print('description: '+grp['description'])
    print('defaultCartType: '+grp['defaultCartType'])
    print('defaultLowCart: '+str(grp['defaultLowCart']))
    print('defaultHighCart: '+str(grp['defaultHighCart']))
    print('cutShelfLife: '+str(grp['cutShelfLife']))
    print('defaultTitle: '+grp['defaultTitle'])
    print('enforceCartRange: '+str(grp['enforceCartRange']))
    print('reportTfc: '+str(grp['reportTfc']))
    print('reportMus: '+str(grp['reportMus']))
    print('')