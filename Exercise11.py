#!/usr/bin/python

# Exercise on prmpting a user to give output

print "How old are you?"
age = int(raw_input())
print "How tall are you?"
height = float(raw_input())
print "How much do you weight?"
weight = int(raw_input())
print "Which is your favourite team"
team = raw_input()

print "You are %d old, %d in height, %d heavy, and your favourite team is %s" % (age, height, weight, team)
