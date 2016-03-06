#!/usr/bin/env python

# Proof of concept example of using the logfs api.
from dronin.logfs import LogFSImport

githash='Release-20160120.3'

imported = LogFSImport(githash, file('magma.bin', 'rb').read())

for obj_name in imported:
    print imported[obj_name]