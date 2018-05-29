# CPE 101 Lab 4
# Name:

def main():
   table_size = get_table_size()
   while table_size != 0:
      first = get_first()
      increment = get_increment()
      show_table(table_size, first, increment)
      table_size = get_table_size()

# Obtain a valid table size from the user
def get_table_size():
   size = input("Enter number of rows in table (0 to end): ")

   while size < 0:
      print "Size must be non-negative."
      size = input("Enter number of rows in table (0 to end): ")
      
   return size;

# Obtain the first table entry from the user 
def get_first():
   first = input("Enter the value of the first number in the table: ")
   
   while first < 0:
      print "First number must be non-negative. "
      first = input("Enter the value of the first number in the table: ")

   return first;

def get_increment():
   increment = input("Enter the increment between rows: ")

   while increment < 0:
      print "Increment must be non-negative."
      increment = input("Enter the increment between rows: ")

   return increment

# Display the table of cubes
def show_table(size, first, increment):
   print "A cube table of size %d will appear here starting with %d." % (size, first)
   print "   Number  Cube "
   
   i = 0
   sumCubes = 0

   while i < size: 
      print "   " + str(first) + "\t   " + str(first **3) 
      i += 1
      sumCubes += first**3
      first += int(increment) 

   print "\nThe sum of cubes is: " + str(sumCubes)
   # Insert Loop Here
   

if __name__ == "__main__":
   main()
