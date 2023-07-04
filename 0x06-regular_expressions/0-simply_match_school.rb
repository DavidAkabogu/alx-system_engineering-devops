#!/usr/bin/env ruby

input = ARGV[0];

if input.nil?
  exit
end

pattern = /School/;
matches = input.scan(pattern)

puts matches.join('');
