#!/usr/bin/perl

use warnings; 
use strict;
use utf8;

while (<>)
{
	if (/^(\P{Ll})(.*)$/) {
		print lc($1) . $2 . "\n";
		next;
	}
	else {
		print;
		next;
	}
}
