#!/usr/bin/python

from sys import exit

def gold_room():
    next0 = raw_input("This room is full of gold. How much do you take?\n")

    if "0" in next0 or "1" in next0:
        how_much = int(next0)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you are not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here"
    print "The bear has a bunch of honey"
    print "The fat bear is in front of another door"
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next1 = raw_input(">>> ")

        if next1 == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next1 == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next1 == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next1 == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means"

def cthulhu_room():
    print "Here you see the great evil Cthulhu"
    print "He, it, whatever stares at you and you go insane"
    print "Do you flee for your life or eat your head?"

    next2 = raw_input(">>> ")

    if "flee" in next2:
        start()
    elif "head" in next2:
        dead("Well that was tasty")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good Job."
    exit(0)


def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next3 = raw_input(">>> ")

    if next3 == "left":
        bear_room()
    elif next3 == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()


