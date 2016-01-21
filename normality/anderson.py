#!/usr/bin/env python2

# Test if data is normally distributed via the Anderson-Darling test.
# https://en.wikipedia.org/wiki/Anderson%E2%80%93Darling_test
#

import sys
import numpy as np
from scipy import stats

from io_helper import open_read

def usage():
    print >> sys.stderr, "{} <source.npy>"
    exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()

    src = sys.argv[1]

    data = np.load(open_read(src))
    A2, critical, sig = stats.anderson(data, dist='norm')
    print >> sys.stderr, "A2: {} Critical Values: {} Sigificance Levels: {}".format(A2, critical, sig)
    if A2 > critical[2]:
        print >> sys.stderr, "Data is not normally distributed"
    else:
        print >> sys.stderr, "Data is normally distributed"


