#!/usr/bin/env python2

# Plot the histogram of the data

import sys
import numpy as np
import matplotlib.pyplot as plt

from io_helper import open_read


def usage():
    print >> sys.stderr, "{} <source.npy>"
    exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()

    src = sys.argv[1]

    data = np.load(open_read(src))
    plt.hist(data)
    plt.show()
