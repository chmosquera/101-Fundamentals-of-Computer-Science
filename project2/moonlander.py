from landerFuncs import *


#Calculates what happens from time zero to laanding
def timePeriod():
   showWelcome()
   time = 0
   flying = True
   altitude = getAltitude()
   currentFuel = getFuel()
   velocity = 0
   acceleration = 0
   displayLMState(time, altitude, velocity, currentFuel, 0) 

   while flying == True:

      if currentFuel > 0:
         FR = getFuelRate(currentFuel)
      else: 
         FR = 0

      currentFuel = fuelUpdate(currentFuel, FR)
      acceleration = updateAcceleration(1.62, FR)
      altitude = updateAltitude(altitude, velocity, acceleration)
      velocity = updateVelocity(velocity, acceleration)
      time += 1
      displayLMState(time, altitude, velocity, currentFuel, FR) 

      if altitude <= 0: #rocket has landed
         flying = False

   print "\n \nStatus at landing - Enjoy your oxygen while it lasts!"

timePeriod()
      
