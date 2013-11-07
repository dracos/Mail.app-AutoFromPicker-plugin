#!/bin/bash

OS_VERSION=`sw_vers -productVersion | grep -o 10\..`

CERT=$1
if [ "$OS_VERSION" == "10.9" ]; then
    : ${CERT:?"You must supply a certificate name"}
fi

rm -rf build dist
/usr/bin/python setup.py py2app
rm -rf ~/Library/Mail/Bundles/AutoFromPicker*.mailbundle

if [ "$OS_VERSION" == "10.9" ]; then
    find dist -print | egrep .so$ | xargs codesign -fv -s "$CERT" > /dev/null
    find dist -print | egrep -i python$ | xargs codesign -fv -s "$CERT" > /dev/null
fi

mv dist/AutoFromPicker*.mailbundle ~/Library/Mail/Bundles/
