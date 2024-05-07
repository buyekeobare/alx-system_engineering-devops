#!/usr/bin/env ruby
# A regular expression that matches a given pattern
# This script accepts one argument and pass it to a regular expression

puts ARGV[0].scan(/hbt*n/).join
