#!/usr/bin/env python

from __future__ import unicode_literals

food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

#STEP 1
print "STEP 1"

likes_format_list = ["{{{key}}} {key}".format(key=key) for key in food_prefs\
                                        if key != "name" and key != "city"]

likes_format_list[-1] = "and " + likes_format_list[-1] + "."

format_string = "{name} is from {city} and he or she likes " + ", ".join(likes_format_list)

print format_string.format(**food_prefs)

#STEP 2
print "STEP 2"
hex_dict = dict(enumerate([hex(i) for i in range(16)]))
print hex_dict

#STEP 3
print "STEP 3"
hex_dict = {i: hex(i) for i in range(16)}

print hex_dict


