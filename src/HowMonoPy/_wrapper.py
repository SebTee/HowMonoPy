from ctypes import *
from sys import platform
import os
import atexit

# map os to correct c library format file
_os_clib_map = {
    "win32": "\\clib\\howmonochromatic.dll",
    "linux": "/clib/libhowmonochromatic.so"
}

# load the c library
_clib_path = os.path.dirname(__file__) + _os_clib_map.get(platform, "")
_clib = CDLL(_clib_path)
_clib.howMono.restype = c_double

# register hs_stop() to be run on program exit
atexit.register(lambda: _clib.hs_exit())

# start haskell
_clib.hs_init(0, 0)


def how_mono(g):
    return _clib.howMono(g.encode())
