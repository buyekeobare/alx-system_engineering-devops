#!/usr/bin/env ruby
# A regular expression that must match school
# This script accepts one argument and pass it to a regular expression

puts ARGV[0].scan(/School/).join
