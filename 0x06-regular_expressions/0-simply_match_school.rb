#!/usr/bin/env ruby
word = ARGV[0]
pattern = /(School)/
match = word.match(pattern)
puts match[1]
