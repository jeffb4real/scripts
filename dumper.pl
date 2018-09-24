#!/usr/bin/env perl

use strict;
use warnings;
use Data::Dumper;

my @arr = (1,2,3,4,5);
print @arr;
print "\n";
print "@arr";
print "\n";
print Dumper @arr;
print "\n";
print Dumper \@arr;

for (my $i = 0; $i < scalar @arr; $i++) {
    print "$arr[$i]\n";
}
