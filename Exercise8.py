#!/usr/bin/python

# Exercise on more and more Printing

formatter = "%r %r %r %r"

print "\n"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it did not sing.",
    "So I said goodnight."
)
