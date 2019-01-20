#!/usr/bin/python

# Exercise on More Files

from sys import argv
from os.path import exists, getsize

script, from_file, to_file = argv

print "\n"
print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)

if exists(to_file) == True:
    print "Read, hit RETURN to continue. CTRL-C to abort"
    raw_input()

    out_file = open(to_file, 'w')
    out_file.write(indata)

    print "Alright! All done"

    out_file.close()
    in_file.close()
    print "The file named", to_file, "is", getsize(to_file), "on size"
    print "\n"
else:
    print "File does not exist...Quiting..."
    print "\n"
    exit()










