#!/usr/bin/env ruby
word = ARGV[0]
pattern = /^(?<!\s)\d{10}\b/
match = word.match(pattern)
puts match
