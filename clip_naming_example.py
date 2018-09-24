#!/usr/bin/python
import os

def run_test(root_dir, mlp_in, clip_list):
	# We've successfully passed "by position" (section 1.3.1 on the confluence page).
	# But if you notice that sometimes you need to pass certain args and other times not pass them,
	# then consider using the pass by "keyword arguments" approach (which can include default values
	# for keyword args that aren't passed to the function).
	print '\nmlp_in: ', mlp_in, '\n'
	for clip in (clip_list):
		full_clip_name = os.path.join(root_dir, clip)
		print full_clip_name

	print "\n\n"
	# An exercise in filename mangling
	for clip in (clip_list):
		full_clip_name = os.path.join(root_dir, clip)
		# head will be the path; tail is all the non-path stuff
		head, tail = os.path.split(full_clip_name)
		name, ext  = os.path.splitext(tail)
		print head + '/' + name + '_reconnected.mlp'


root_dir = 'c:/temp'
mlp_in = 'ABC.mlp'
clip_list = ('clipA', 'clipB', 'clipC')
# I think no need to defined the following explicitly, as the names can be formed based on mlp_in
# connected_mlp_out = 
# decoded_wav_out = 
run_test(root_dir, mlp_in, clip_list)
