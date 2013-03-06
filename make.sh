#!/bin/bash
rm -rf build dist
/usr/bin/python setup.py py2app
rm -rf ~/Library/Mail/Bundles/AutoFromPicker.mailbundle
mv dist/AutoFromPicker.mailbundle ~/Library/Mail/Bundles/

