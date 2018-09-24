#!/usr/bin/perl
use strict;
use warnings;
my $apples = 4;
my $oranges = 7;
my $pears = 3;
print <<'EOT';
My fruit list:
	"$apples" apples
	$oranges oranges
	$pears pears
EOT

# This is the Python way of block printing
#  fat_cat = """
#  I'll do a list:
#  \t* Cat food
#  \t* Fishies
#  \t* Catnip\n\t* Grass
#  """