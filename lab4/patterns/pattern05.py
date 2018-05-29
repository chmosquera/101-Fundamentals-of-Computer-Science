import driver

def letter(row, col):
	n=0
	if (row > col):
		return 'T'
	else:
		return 'W'
	n=+1

if __name__ == '__main__':
   driver.comparePatterns(letter)
