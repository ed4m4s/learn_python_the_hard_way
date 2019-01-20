#!/usr/bin/python

# Exercise on Reading and Writing files

# Give it an argument before run it. Be aware it will delete the contents of the filename.

# Import the argv feature from the sys module.
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you do not want that hit CTRL-C (^C) NOW."
print "If you do want that hit RETURN."

raw_input("?")

# Open the file first.
print "Opening the file..."
target = open(filename, 'w')

# Truncating means delete the contents........Not the file.
print "Truncating the file now. Goodbye!"
target.truncate()

print "Now I am going to ask you for three lines"

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I am going to write those lines above on a new file."

# Write the new lines on the file.
target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

# Close the file each time you open it for good practice.
print "And finally, we close the file."
target.close()

