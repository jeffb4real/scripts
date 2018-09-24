#!/usr/bin/env python

# http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html

dum = ('1861-10-23', ['poetry', 'pretend-fight'])
dee = ('1861-10-23', ['poetry', 'pretend-fight'])
print

print 'type(dum): ', type(dum)
print 'type(dee): ', type(dee)
print 'id(dum): ', id(dum)
print 'id(dee): ', id(dee)
print 'value dum: ', dum
print 'value dee: ', dee
print 'dum == dee: ', dum == dee
print 'dum is dee: ', dum is dee
print

t_doom = dum
print 'type(t_doom): ', type(t_doom)
print 'id(t_doom): ', id(t_doom)
print 'value t_doom: ', t_doom
print 't_doom == dum: ', t_doom == dum
print 't_doom is dee: ', t_doom is dum
print

skills = t_doom[1]
skills.append('rap')
print 'value t_doom: ', t_doom
print 'value dum: ', dum
print

