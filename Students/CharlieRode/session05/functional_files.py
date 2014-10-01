#!/usr/bin/env python

import io, sys

def clean_file(filename, overwrite= False):
    f= io.open(filename, 'r+')
    f.seek(0)
    lines= f.readlines()
    f.close()
    if overwrite:
        f= io.open(filename, 'w')
        f.write(u'\n'.join(map(lambda x: x.strip(), lines)))
        f.close()
    else:
        new_file= 'clean_text.txt'
        f= io.open(new_file, 'w')
        f.write(u'\n'.join(map(lambda x: x.strip(), lines)))
        f.close()


def cleaner_file(filename, overwrite= False):
    f= io.open(filename, 'r+')
    f.seek(0)
    lines= f.readlines()
    f.close()
    if overwrite:
        f= io.open(filename, 'w')
        f.write(u'\n'.join(line.strip() for line in lines))
        f.close()
    else:
        new_file= 'clean_text.txt'
        f= io.open(new_file, 'w')
        f.write(u'\n'.join(line.strip() for line in lines))
        f.close()

if __name__ == '__main__':

    filename= sys.argv[1]

    while True:
        string=  raw_input("Do you want to [O]verwrite the existing file, or create a [N]ew file?").lower()
        if string== "o":
            clean_file(filename, True)
            break
        elif string== "n": 
            clean_file(filename)
            break
        