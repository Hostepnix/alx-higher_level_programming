#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'w') as fd:
        return fd.write(text)
