#!/usr/bin/env ruby
# A regular expression that matches school
# This script accepts one argument and pass it to a regular expression

puts ARGV[0].scan(/School/).join
