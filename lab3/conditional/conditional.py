#Name: Chanelle Mosquera
#Section: 101-16
#Description: Functions with If Statements
#Instructor: S. Einakian
#Due date: Jan. 21, 2016

def max_101(x,y):
   if x > y:
      return x
   elif y > x:
      return y
   else:
       return False

def max_of_three(x,y,z):
   if float(x) > float(z) and float(x) > float(y):
      return float(x)
   elif float(y) > float(x) and float(y) > float(z):
      return float(y)
   elif float(z) > float(x) and float(z) > float(y):
      return float(z)

def rental_late_fee(days_late):
   if days_late <= 0:
      fee = 0
   if 0 < days_late <= 9:
      fee = 5
   if 9 < days_late <= 15:
      fee = 7
   if 15 < days_late <= 24:
      fee = 19
   if days_late > 24:
      fee = 100
   return fee

print rental_late_fee(0)
print rental_late_fee(7)
print rental_late_fee(10)
print rental_late_fee(23)

print rental_late_fee(30)

