#Name: Chanelle Mosquera
#Section: 101-16

import funcs
import math

def main():
   pounds = float(input('How much do you weigh (pounds)? '))
   distance = float(input('How far away is your professor (meters)? '))
   object = raw_input('Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? \n')

   massSkater = funcs.poundsToKG(pounds)
   massObject = funcs.getMassObject(object)
   velObject = funcs.getVelocityObject(distance)
   velSkater = funcs.getVelocitySkater(massSkater, massObject, velObject)

   print 'Nice throw!',   
   if massObject <= 0.1:
      print "You're going to get an F!"
   elif massObject > 0.1 and massObject <= 1.0:
      print "Make sure youre professor is OK."
   elif massObject > 1.0 and distance  < 20:
      print "How far away is the hospital?"
   elif massObject > 1.0 and distance  >= 20:
      print "RIP professor."

   print "Velocity of skater: ", ("%.3f" % velSkater), "m/s"
   if velSkater < 0.2:
      print "My grandmother skates faster than you!"   
   if velSkater >= 0.2 and velSkater < 1.0:
      print ""
   if velSkater >= 1.0:
      print "Look out for that railing!!!"


#Code here

if __name__ == '__main__':
   main()
