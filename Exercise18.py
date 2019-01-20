#!/usr/bin/python

# Exercise on Names, Variables, Code, Functions

# this one is like the scripts we did with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# Take out the *args as you do not need it
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# Takes one argument only
def print_one(arg1):
    print "arg1: %r" % arg1

# No arguments at all.
def print_none():
    print "I got no arguments"

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

