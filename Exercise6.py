#!/usr/bin/python

# Exercise on Strings and Text

# Setting up some variables
x = "There are %d types pf people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

# Printing the x and y variable from above.
print "\n"
print x
print y

print "I said: %r." % x         # we use %r for debugging since it displays the "raw" data of the variable.
print "I also said: '%s'." % y

# More variables and printing
hilarious = False
joke_evalution = "Isn't that joke so funny?! %r"

print joke_evalution % hilarious

w = "this is the left side of..."
e = "a string with a right side."

print w + e

