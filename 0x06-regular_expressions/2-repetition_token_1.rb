#!/usr/bin/env ruby
word = ARGV[0]
pattern = /\b(hbtn|hbn|htn)\b/
match = word.match(pattern)
puts match
