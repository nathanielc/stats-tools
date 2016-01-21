import sys
from cStringIO import StringIO

def open_read(filename):
    """
    Open a file for reading.
    If the filename is '-' open STDIN
    """
    if filename == '-':
        return StringIO(sys.stdin.read())
    return open(filename, 'rb')

def open_write(filename):
    """
    Open a file for writing.
    If the filename is '-' open STDOUT
    """
    if filename == '-':
        return sys.stdout
    return open(filename, 'wb')
