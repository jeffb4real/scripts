#!/usr/bin/python
# There is a grid of size M x N.  The top left corner is (0,0) and the bottom right is (m-1,n-1).  
# Write a function to print all the paths from (0,0) to (m-1,n-1), where you can only move right or down, no backtracking.  
# For example, in a 2x2 grid, the function should print "D,R" and "R,D" because there are only two possible paths
# from the top left to the bottom right.

import sys
import time

def print_paths(x,y,m,n,full_path):
	if x == m - 1 and y == n - 1:
		print full_path
		return
	if x < m - 1:
		print_paths(x + 1, y, m, n, str(full_path) + 'r')
	if y < n - 1:
		print_paths(x, y + 1, m, n, str(full_path) + 'd')

# Ex. 1: 10 x 20 grid
M = 10
N = 20
#try:
#	M = int(sys.argv[1])
#	N = int(sys.argv[2])
#except:
	
if not M or not N:
	print '\nUsage:\n\tmbyn_recursion.py arg1=M arg2=N\n'
	exit()
start = time.time()
print_paths(0,0,M,N,'')
end = time.time()

hours, rem = divmod(end - start, 3600)
minutes, seconds = divmod(rem, 60)
print "Elapsed time: {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)

# 00:00:36.87
