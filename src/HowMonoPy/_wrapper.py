from ctypes import *
import os

_module_dir = os.path.dirname(__file__)
_clib_path = _module_dir + "/clib/libhowmonochromatic.so"
_clib = CDLL(_clib_path)
_clib.howMono.restype = c_double


class Analyser:
    def __init__(self):
        self._clib = _clib

    def __enter__(self):
        self._clib.hs_init(0, 0)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._clib.hs_exit()

    def how_mono(self, g):
        return self._clib.howMono(g.encode())
