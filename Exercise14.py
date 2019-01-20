#!/usr/bin/python

# Exercise on Prompting and Passing

from sys import argv

print "\n"
script, user_name = argv
prompt = '>>> '

print "Hi %s, I am the %s script" % (user_name, script)
print "I would like you to ask few questions"

print "Do you like me %s" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have %s?" % user_name
computer = raw_input(prompt)

print "Are you learning Python programming? %s" % user_name
programming = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where it is that.
And you have a %r computer. Nice.
Also you said %r in the question if you learn Python.
""" % (likes, lives, computer, programming)

