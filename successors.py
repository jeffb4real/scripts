#!/usr/bin/python

# Write a function that takes in an integer array and returns an integer.  The function should return the element in the array that has the 
# maximum number of "successors".  A "successor" is an element that comes after the current element AND is strictly greater than the 
# current element.  You can assume that every integer in the array is unique, and that if there is a tie for maximum number of successors, 
# it doesn't matter which one is returned.  So for example, the array [4,6,1,8] has successors 2,1,1, and 0.  
# (4 has successors 6 and 8, 6 has successor 8, etc.).  In this case you would return "4".

def find_max_successors(a_list):
	successor_list = []
	length = len(a_list)
	print 'list: ', a_list
	for i, item in enumerate(a_list):
		print i, item
		r1 = i + 1
		num_successors = 0
		for j in range(r1, length):
			print '  %d' % (a_list[j])
			if item < a_list[j]:
				num_successors = num_successors + 1
		successor_list.append(num_successors)

	print '\nsuccessor list: ', successor_list

	return a_list[successor_list.index(max(successor_list))]


a_list = [4, 6, 1, 8]
print 'element having max successors: %d\n\n' % find_max_successors(a_list)
a_list = [4, 6, 1, 8, 0]
print 'element having max successors: %d\n\n' % find_max_successors(a_list)
a_list = [8, 4, 2]
print 'element having max successors: %d\n\n' % find_max_successors(a_list)
a_list = [12, 11, 10, 7, 1, 2, 3, 12]
print 'element having max successors: %d\n\n' % find_max_successors(a_list)
