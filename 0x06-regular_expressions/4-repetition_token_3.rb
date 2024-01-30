#!/usr/bin/env ruby
word = ARGV[0]
pattern = /hbt*n/
match = word.match(pattern)
puts match
