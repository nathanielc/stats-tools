#!/usr/bin/env python2

# Try to find a power transformation that will make the data normally distributed,
# using the Box-Cox method.
# https://en.wikipedia.org/wiki/Power_transform

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from io_helper import open_write,open_read

def usage():
    print >> sys.stderr, "{} <source.npy> [output.npy]"
    exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()

    src = sys.argv[1]
    out = None
    if len(sys.argv) == 3:
        out = sys.argv[2]

    data = np.load(open_read(src))
    if data.min() <= 0:
        data += data.min() + 1
    boxcox, l = stats.boxcox(data)
    print >> sys.stderr, "Lambda: {}".format(l)
    if out is not None:
        np.save(open_write(out), boxcox)
