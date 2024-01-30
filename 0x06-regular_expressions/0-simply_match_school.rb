#!/usr/bin/env ruby
word = ARGV[0]
pattern = /(School)/
match = word.match(pattern)
if match
  puts match[1]
end
