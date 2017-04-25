#!/usr/bin/env python
# -*- coding: utf8 -*-

class Robot:
    """represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """initialized the data."""
        self.name = name
        print "initializing {}".format(self.name)

        # when this poerson is created, the robot adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print "{} is being destroyed!".format(self.name)
        Robot.population -= 1

        if Robot.population == 0:
            print '{} was the last one.'.format(self.name)
        else:
            print "There are still {:d} robots working.".format(Robot.population)

    def say_hi(self):
        """greeing by the robot

yeh, they can do that."""
        print 'greetings, my masters call me {}.'.format(self.name)
        
    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print 'we have {:d} robots.'.format(cls.population)


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print "robots can do some work here.\n"

print "robots have finished their work. so let's destroy them."

droid1.die()
droid2.die()

Robot.how_many()

droid1.die()

Robot.how_many()

print Robot.population
