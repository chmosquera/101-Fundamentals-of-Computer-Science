# Project 2 - Moonlander
# Author: 
# Version: 

def showWelcome():
   print "\n Welcome aboard the Lunar Module Flight Simulator \n \n \t To begin you must specify the LM's initial altitude \n \t and fuel level. To simulate the actual LM use \n \t values of 1300 meters and 500 liters, respectively. \n \n \t Good luck and may the force be with you! \n"

def getFuel():
   initialFuel = input("Enter the initial amount of fuel on board the LM (in liters): ")
   
   while initialFuel <= 0:
      print "ERROR: Amount of fuel must be positive, please try again"
      initialFuel = input("Enter the initial altitude of the LM (in meters): ")

   return initialFuel

def getAltitude():
   initialAlt = input("Enter the initial altitude of the LM (in meters): ")
  
   while initialAlt <= 0 or initialAlt >= 9999:
      print "ERROR: Altitude must be between 1 and 9999, inclusive, please try again"
      initialAlt = input("Enter the initial amount of fuel on board the LM (in liters): ")

   return initialAlt

   
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):   
   
   e = "\nElapsed Time: \t " + str(elapsedTime) + " s"
   a = "\n    Altitude: \t " + str("%.2f" %altitude) + " m"
   v = "\n    Velocity: \t " + str("%.2f" %velocity) + " m/s"
   fA = "\n        Fuel: \t " + str(fuelAmount) + " l"
   fR = "\n        Rate: \t " + str(fuelRate) + " l/s"

   if fuelAmount > 0:
      print "\nLM state at retrorocket cutoff" + e + fA + fR + a + v + "\n"
   elif fuelAmount == 0 and altitude == 0:
      print "\nLM state at landing/impact" + e + fA + fR + a + v
   else: 
      print "OUT OF FUEL - Elapsed Time: \t " + str(elapsedTime) + " Altitude: \t " + str("%.2f" %altitude) + " Velocity:   " + str("%.2f" %velocity)

def getFuelRate(currentFuel):
   fuelRate = input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): ")

   while fuelRate < 0 or fuelRate >9:
      print "ERROR: Fuel rate must be between 0 and 9, inclusive"
      fuelRate = input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): ")

   if fuelRate <= currentFuel:
      return fuelRate
   else:
      return currentFuel

def fuelUpdate(currentFuel, fuelRate):
   newFuel = currentFuel - fuelRate
   return max(newFuel, 0)
 
def updateAcceleration(gravity, fuelRate):
   acceleration = gravity * ((float(fuelRate) / 5) - 1)
   return acceleration
	
def updateAltitude(altitude, velocity, acceleration):
   alt = altitude + velocity + (float(acceleration) / 2)
   return max(alt, 0)

def updateVelocity(velocity, acceleration):
   vel = velocity + acceleration
   return vel

def updateFuel(fuel, fuelRate):
   f = fuel - fuelRate
   return f

def displayLMLandingStatus(velocity):
   if velocity <= 0 and velocity >= -1:
      print "Status at landing - The eagle has landed!"
   elif velocity <= -1 and velocity >= -10:
      print "Status at landing - Enjoy your oxygen while it lasts!"
   elif velocity <= -10:
      print "Status at landing - Ouch - that hurt!"


