#!/usr/bin/python3

s = "am a boy"
print("The address of {} is {}".format(s, id(s)))
s += s
print("The address of {} is {}".format(s, id(s)))
