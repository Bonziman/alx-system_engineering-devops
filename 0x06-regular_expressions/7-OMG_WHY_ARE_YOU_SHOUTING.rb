#!/usr/bin/env ruby
word = ARGV[0]
pattern = /[A-Z]*/
match = word.scan(pattern)
puts match.join
