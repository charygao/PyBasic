from __future__ import print_function
import os
from os.path import join, getsize


def getFileSize(file):
    size = getsize(file)

    return size

if __name__ == '__main__':
    print (getFileSize('Basic_3/fileSize.py'))
