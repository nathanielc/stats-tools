#!/usr/bin/env python2

#
# Query data from InfluxDB and save it as a numpy .npy file
#

import sys
import numpy as np
from influxdb import InfluxDBClient

from io_helper import open_write


def usage():
    print >> sys.stderr, "{} <query> <output>".format(__file__)
    exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()

    query = sys.argv[1]
    out = sys.argv[2]

    client = InfluxDBClient('localhost', 8086, 'root', 'root', '')
    result = client.query(query)

    for rs in result:
        cols = [k for k in rs[0].keys() if k != 'time']
        cols_count = len(cols)
        data = np.zeros((len(rs), cols_count))
        r = 0
        for row in rs:
            c = 0
            for col in cols:
                data[r,c] = row[col]
                c += 1
            r += 1

        if len(data.shape) == 2 and data.shape[1] == 1:
            data = data.reshape(data.shape[0])
        np.save(open_write(out), data)








