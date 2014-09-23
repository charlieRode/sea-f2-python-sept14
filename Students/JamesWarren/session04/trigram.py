#!/usr/bin/env python

import io

sherlock = io.open('sherlock.txt', mode='r')

#iterator skips header and table of contents at beginning of file
for i in range(61):
    sherlock.readline()

#save all text after header and table of contents to "source"
source = sherlock.read()
sherlock.close()

source = source.split()

source_dict = {}

#loops through text, creates dictionary sets of "word1 word2 : word3"
for i in range(len(source)-3):
    source_dict.setdefault("%s %s" % (source[i], source[i+1]), []).append(source[i+2])

trigram = ["This", "is"]



for i in range(1000):
    if source_dict.get((" ").join(trigram[-2:])):
        trigram = trigram.append(source_dict[trigram[-2:]])

##86
#for key in source_dict.keys((" ").join(trigram[-2:])):
#    if (" ").join(trigram[-2:]) == key:
#        trigram = trigram.append(source_dict[key])
#86

print trigram
    #find key of trigram[:-2] + trigram[:-1], .append(value of key) to trigram