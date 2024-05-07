#!/usr/bin/env ruby
# A regular expression that must match only capital letters
 
puts ARGV[0].scan(/[A-Z]/).join
