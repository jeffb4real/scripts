#!/usr/bin/python
# There is a grid of size M x N.  The top left corner is (0,0) and the bottom right is (m-1,n-1).  
# Write a function to print all the paths from (0,0) to (m-1,n-1), where you can only move right or down, no backtracking.  
# For example, in a 2x2 grid, the function should print "D,R" and "R,D" because there are only two possible paths
# from the top left to the bottom right.

# Make an assumption: No matter the size of M and N, each valid path will have the same number of steps.
import sys
import time

def test_valid_path(this_path):
	x = y = 0
	for j in this_path:
		if int(j) == 0:
			x = x + 1
		else:
			y = y + 1
	if ((x == M - 1) and (y == N - 1)):
		return 1
	else:
		return 0

#M = int(sys.argv[1])
#N = int(sys.argv[2])
M = int(raw_input('M: '))
N = int(raw_input('N: '))

numsteps = M + N - 2
numpaths = pow(2, numsteps)
format_length = '0' + str(numsteps) + 'b'
#print 'numsteps =', numsteps
#print 'numpaths =', numpaths
#print 'format_length =', format_length

start = time.time()

for j in range(0, numpaths):
	# Convert int into binary string
	bin_string = format(j, format_length)
	if test_valid_path(bin_string):
		print ''
		# Iterate over each digit in binary string
		for k in bin_string:
			if int(k) == 0:
				sys.stdout.write('r')
			else:
				sys.stdout.write('d')

end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("\n\n{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))

