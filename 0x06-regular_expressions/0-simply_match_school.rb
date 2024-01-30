#!/usr/bin/env ruby
word = ARGV[0]
pattern = /(S+c+h+o+o+l)/
match = word.match(pattern)
if match
    puts match[1]
end
