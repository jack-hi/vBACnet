#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
misc.py
"""
from os import remove
from commons import addlog, init_log
from time import sleep

_debug = True

@addlog
class Vdev:
    """
    Using a file to simulate a dev.
    """
    def __init__(self, file, mode='wb'):
        if _debug: Vdev.debug("Vdev: create file: %s[%s]" % (file, mode))
        self.file = file
        self.mode = mode
        self.dev = open(file, 'wb').close()

    def __del__(self):
        if _debug: Vdev.debug("    - Vdev: destory file: %s" % self.file)
        if self.dev is not None:
            self.dev.close()
        remove(self.file)


if __name__ == '__main__':
    init_log(level="DEBUG")
    v = Vdev("test")
    sleep(2)
    del v

