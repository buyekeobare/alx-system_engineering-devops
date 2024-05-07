#!/usr/bin/env ruby
# A regular expression that matches a given pattern
# This script outputs script should output: [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
