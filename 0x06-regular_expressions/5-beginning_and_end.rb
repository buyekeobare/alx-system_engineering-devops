#!/usr/bin/env ruby
# A regular expression that matches a string that starts with h ends with n and can have any single character in between
# This script accepts one argument and pass it to a regular expression

puts ARGV[0].scan(/h.n/).join
