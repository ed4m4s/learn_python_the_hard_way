#!/usr/bin/python

# Exercise on Else if statements

people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars"
elif cars < people:
    print "We should not take the cars"
else:
    print "We cant decide"

if buses > cars:
    print "Thats too many buses"
elif buses < cars:
    print "Maybe we could take the buses"
else:
    print "We still cannot decide"

if people > buses:
    print "Alright, let's just take the buses"
else:
    print "Fine, let's stay home then."

