from distutils.core import setup
import py2exe
import sys

sys.argv.append("py2exe")

setup(windows=[{'script': 'cicfighters.py', 'icon_resources': [(1, "cicfighters-large.ico")]}],
     options = {'py2exe': {'optimize': 1, 'bundle_files':1} },
     zipfile=None)
