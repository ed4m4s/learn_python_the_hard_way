#!/usr/bin/python

# Exericse on Functions and Variables

# Defining a Variable named cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# Pass variables to the function above
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Setting our own variables and pass them to the function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Do some math before
print "We can even do some math inside too."
cheese_and_crackers(10 + 20, 5 + 6)

# Do some math with the variables
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_cheese + 1000)


def my_own_script(x, y):
    print x, y

my_own_script(30, 89)



