# AutoFromPicker plugin for Mail.app
# (C) Copyright 2012 Matthew Somerville
# Based on Attachment Scanner Plugin by James R. Eagan (code at my last name dot me)
# Nagging and whining and unreliable maintaining by Stefan Magdalinski (stefan at whitelabel.org)
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# and GNU Lesser General Public License along with this program.  
# If not, see <http://www.gnu.org/licenses/>.
from distutils.core import setup
import py2app

import platform

# If running gives a 'disabled plugin' error, then I missed out some Mail
# version UUIDs from the list; you have to provide for every version of Mail
# you want your plugin to run under. Find yours by running, before 10.9:
#   defaults read /System/Library/Frameworks/Message.framework/Resources/Info PluginCompatibilityUUID
#   defaults read /Applications/Mail.app/Contents/Info PluginCompatibilityUUID
# OR in 10.9:
#   defaults find UUID | grep MailCompatibility
#   defaults find UUID | grep MessageCompatibility
# and adding those two strings to the list below.

VERSION='0.4'
COPYRIGHT='Copyright 2013, Matthew Somerville'

plist = dict(NSPrincipalClass='AutoFromPicker',
             CFBundleGetInfoString=\
              'Auto From Picker plugin version %s, %s' % (VERSION, COPYRIGHT),
             CFBundleIdentifier='uk.co.dracos.AutoFromPicker',
             CFBundlePackageType='BNDL',
             CFBundleShortVersionString=VERSION,
#             CFBundleVersion=VERSION,
             NSHumanReadableCopyright=COPYRIGHT,
             SupportedPluginCompatibilityUUIDs=['225E0A48-2CDB-44A6-8D99-A9BB8AF6BA04', # Mail 4.0
                                                'B3F3FC72-315D-4323-BE85-7AB76090224D', # Message 4.0
                                                '2610F061-32C6-4C6B-B90A-7A3102F9B9C8', # Mail 4.1
                                                '99BB3782-6C16-4C6F-B910-25ED1C1CB38B', # Message 4.1
                                                '2F0CF6F9-35BA-4812-9CB2-155C0FDB9B0F', # Mail 4.2
                                                '0CB5F2A0-A173-4809-86E3-9317261F1745', # Message 4.2
                                                'B842F7D0-4D81-4DDF-A672-129CA5B32D57', # Mail 4.3
                                                'E71BD599-351A-42C5-9B63-EA5C47F7CE8E', # Message 4.3
                                                'BDD81F4D-6881-4A8D-94A7-E67410089EEB', # Mail 4.4
                                                '857A142A-AB81-4D99-BECC-D1B55A86D94E', # Message 4.4
                                                '1C58722D-AFBD-464E-81BB-0E05C108BE06', # 10.6.7 (4.5)
                                                '9049EF7D-5873-4F54-A447-51D722009310', # 10.6.7 (4.5)
                                                '36555EB0-53A7-4B29-9B84-6C0C6BACFC23', # Mail 4.4.1?
                                                '6E7970A3-E5F1-4C41-A904-B18D3D8FAA7D', # Mail 5.1
                                                'EF59EC5E-EFCD-4EA7-B617-6C5708397D24', # Message 5.1
                                                '4C286C70-7F18-4839-B903-6F2D58FA4C71', # Mail 5.2 (upto 10.7.4)
                                                '3335F782-01E2-4DF1-9E61-F81314124212', # Messages 5.3
                                                '758F235A-2FD0-4660-9B52-102CD0EA897F', # Mail 5.3 (10.7.5)
                                                '1146A009-E373-4DB6-AB4D-47E59A7E50FD', # Messages 6.0 ( 10.8.0 )
                                                '608CE00F-4576-4CAD-B362-F3CCB7DE8D67', # Mail 6.0 ( 10.8.0 )
                                                '2183B2CD-BEDF-4AA6-AC18-A1BBED2E3354', # Messages 6.? ( 10.8.4 )
                                                '19B53E95-0964-4AAB-88F9-6D2F8B7B6037', # Mail 6.? ( 10.8.4 )
                                                '0941BB9F-231F-452D-A26F-47A43863C991', # Mail 7.0 ( 10.9.0 )
                                                'FBE5B158-5602-4A6D-9CC5-8461B9B7054E', # Mail 7.0 (1822)
                                                '1CD40D64-945D-4D50-B12D-9CD865533506', # Mail 7.1 (1827)
                                                '88ED2D4C-D384-4BF5-8E94-B533455E6AAF', # Mail 7.2 (1874)
                                                'F4C26776-22B3-4A0A-96E1-EA8E4482E0B5', # Mail 7.3 (1878.2)
                                                'D1EFE124-86FF-4751-BF00-80B2C0D6F2E4', # Mail 7.3 (1878.6)

                                               ]

        )

OS_VERSION = platform.mac_ver()[0]

if OS_VERSION >= '10.9':
    plugin = ['AutoFromPicker-10.9.py']
else:
    plugin = ['AutoFromPicker.py']
setup(
    plugin = plugin,
    options = dict(py2app=dict(extension='.mailbundle', plist=plist))
 )  
