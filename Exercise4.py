#!/usr/bin/python

# Exercise on Variables and Names

# Setting up variables

cars = 100
space_in_a_car = 4.0
drivers = 30
passangers = 90

# Setting up some further variables that are based from the variables above
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passangers_per_car = passangers / cars_driven

# Printing out on the console the variables from above.
print "\n"
print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passangers, "to carpool today"
print "We have to put about", average_passangers_per_car, "in each car"

