#!/usr/bin/env python2
""" https://github.com/cheran-senthil/PyRival <hello@cheran.io> """
from __future__ import division, print_function

import os
import sys
from atexit import register
from cStringIO import StringIO
from itertools import ifilter, imap, izip

range = xrange
filter, map, zip = ifilter, imap, izip

sys.stdout = StringIO()
register(lambda: os.write(1, sys.stdout.getvalue()))
input = StringIO(os.read(0, os.fstat(0).st_size)).readline


def main():
    pass


if __name__ == '__main__':
    main()
