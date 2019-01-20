#!/usr/bin/python


# My Script to delete the contents of a file but prompting the user first.
from sys import argv

script, filename = argv

print "\n"
response = raw_input("Do you really want to delete the contents of this %r file? (Yy/Nn) " % filename)

if response == "Y" or response == "y":
    target = open(filename, 'w')
    target.truncate()
    target.close()
elif response == "N" or response == "n":
    print "Exiting ........"
    exit()












