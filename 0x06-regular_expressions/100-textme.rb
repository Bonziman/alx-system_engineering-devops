#!/usr/bin/env ruby
string = ARGV[0]
sender_pattern = /\[from:([^\]]+)\]/
reciever_pattern = /\[to:([^\]]+)\]/
flags_pattern = /\[flags:([^\]]*)\]/

sender = string.match(sender_pattern)
reciever = string.match(reciever_pattern)
flags = string.match(flags_pattern)

puts "#{sender[1]},#{reciever[1]},#{flags[1]}"
