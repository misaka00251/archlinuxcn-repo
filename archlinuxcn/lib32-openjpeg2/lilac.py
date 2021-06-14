#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='oxalin')
    add_provides(['libopenjp2.so'])

def post_build():
    check_library_provides()
    aur_post_build()
