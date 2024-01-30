#!/usr/bin/env ruby
word = ARGV[0]
pattern = /(h+b+t{2,5}+n)/
match = word.match(pattern)
puts match
