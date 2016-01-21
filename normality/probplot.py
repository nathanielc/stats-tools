#!/usr/bin/env python2

# Plot the probability plot of the data against the normal distribution.

import sys
import numpy as np
from scipy import stats
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
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    prob = stats.probplot(data,dist=stats.norm,plot=ax1)
    ax1.set_title("Probability plot for normal distribution")
    plt.show()
