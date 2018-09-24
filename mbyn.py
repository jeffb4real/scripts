#!/usr/bin/env python
# There is a grid of size M x N.  The top left corner is (0,0) and the bottom right is (m-1,n-1).  
# Write a function to print all the paths from (0,0) to (m-1,n-1), where you can only move right or down, no backtracking.  
# For example, in a 2x2 grid, the function should print "D,R" and "R,D" because there are only two possible paths
# from the top left to the bottom right.

# Make an assumption: No matter the size of M and N, each valid path will have the same number of steps.

def test_valid_path(this_path):
	m = n = 0
	for j in this_path:
		if int(j) == 0:
			m = m + 1
		else:
			n = n + 1
	#print 'm, n =', m, n
	if ((m == M - 1) and (n == N -1)):
		return 1
	else:
		return 0

M = int(raw_input('M: '))
N = int(raw_input('N: '))

numsteps = M + N - 2
print 'numsteps =', numsteps
numpaths = pow(2, numsteps)
print 'numpaths =', numpaths
format_length = '0' + str(numsteps) + 'b'
print 'format_length =', format_length

for j in range(0, numpaths):
	bin_string = format(j, format_length)
	print '\n',
	for k in bin_string:
		if int(k) == 0:
			print 'r',
		else:
			print 'd',
	if test_valid_path(bin_string):
		print ' <-- pass',




