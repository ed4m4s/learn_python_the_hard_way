#!/usr/bin/python

# Exercise on more Variables and Printing

#Setting up some variables includying strings and numbers
my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

multiply1 = 10
multiply2 = 5
multiply3 = 45


my_floating_point = 1.437592

# Printing those variables from above as well as formatters (i.e. %s, %d, %r)
print "\n"
print "Let's talk about %s" % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy" % my_weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are usually %s depending on the office." % my_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "If I multiply %d, and %d together with %d I will get %d" % (multiply1, multiply2, multiply3, multiply1 * multiply2 * multiply3)

my_name_is = 'ed4m4s'
print "My name is %r" % my_name_is # the "r" here means print this no matter what

print "Floating round the number 1.437592 is", round(my_floating_point)
