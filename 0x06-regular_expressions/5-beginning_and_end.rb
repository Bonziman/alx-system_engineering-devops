#!/usr/bin/env ruby
word = ARGV[0]
pattern = /h(.)n/
match = word.match(pattern)
puts match
