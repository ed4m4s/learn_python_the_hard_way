#!/usr/bin/python

# Exercise on While-Loops
# Adding to a list within a while loop

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numnbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num

#############------------Practice-------------###############

# Adding to a list within a while loop by calling a function though


#def while_loop(x):
#    i = 0
#    numbers = []
#    while i < x:
#        print "At the top i is %d" % i
#        numbers.append(i)

#        i = i + 1
#        print "Numnbers now: ", numbers
#        print "At the bottom i is %d" % i
#
#    return numbers

#my_numbers = while_loop(10)
#print "\n"
#print "The numbers after the loop are: ", my_numbers
