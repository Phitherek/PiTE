#!/usr/bin/python2
# PitE, Piotr Zurek, Lab 1, Zad 1
import os
import sys
import stat

def make_listing(path, curdepth, maxdepth):
    try:
        mode = os.stat(path).st_mode # Sprawdzamy typ pliku
        if stat.S_ISDIR(mode) != 0 and stat.S_ISLNK(mode) == 0: # Katalog
            print ('  ' * curdepth) + "Directory: " + path
            if curdepth == maxdepth:
                print ('  ' * curdepth) + "Tree depth exceeded..."
            else:
                dirlist = os.listdir(path)
                for p in dirlist:
                    make_listing(path + "/" + p, curdepth+1, maxdepth)
        elif stat.S_ISREG(mode): # Plik
            print ('  ' * curdepth) + os.path.basename(path)
    except OSError:
        print ('  ' * curdepth) + "Could not list directory..."

directory = None
maxdepth = None
if len(sys.argv) == 1:
    directory = os.environ.get("HOME") # Pobieramy katalog domowy
    maxdepth = 20 # Maksymalne zagniezdzenie rekursji
elif len(sys.argv) == 2:
    directory = sys.argv[1]
    maxdepth = 20
else:
    directory = sys.argv[1]
    maxdepth = int(sys.argv[2])
make_listing(directory, 0, maxdepth) # Rekursywnie listujemy katalog domowy
