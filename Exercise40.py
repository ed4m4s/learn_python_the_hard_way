#!/usr/bin/python

# Exercise on Modules, Classes and Ogjects

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I do not want to get sued",
                   "So I will stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

print "\n"





# My Class
print "What is your name?"
myname = raw_input(">>> ")
print "What is your surname"
mysurname = raw_input(">>> ")
print "What is your profession"
myprofession = raw_input(">>> ")

class ed4m4s(object):

    def __init__(self, name, surname, profession, x):
        self.name = name
        self.surname = surname
        self.profession = profession
        self.x = x + 10

thing = ed4m4s(myname, mysurname, myprofession, 900)
print "Your name is %s, your surname is %s, and you are a(n) %s" % (thing.name, thing.surname, thing.profession)
print thing.x





