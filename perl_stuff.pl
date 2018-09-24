#!/usr/bin/perl

use strict;            # better error checking
use warnings;          # better warnings
use File::Basename;    # fileparse()
use Data::Dumper;
#use Switch;            # switch...case

my $var = 'jeff';

if ($var =~ /ef/) {
    print "match\n";
}

