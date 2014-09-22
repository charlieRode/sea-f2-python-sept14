#!/usr/local/bin/python

import urllib#, string
import random, textwrap


base_text_file = urllib.urlopen(u"http://codefellows.github.io/sea-c15-python/_downloads/sherlock.txt")

base_text = base_text_file.read()

base_text_file.close()

#Maybe do some cleanup here; need to look more carefully at the file to figure that out

# extra_punctuation = string.punctuation.strip("'-") #Leave some in

# base_text = base_text.strip(extra_punctuation)

base_list = base_text.split()

trigrams = {} #Each key will be a pair of words, and the value will be a list of words that follow that pair

for i in range(len(base_list) - 2):
    key = " ".join(base_list[i:i+2])
    if trigrams.has_key(key):
        trigrams[key].append(base_list[i+2])
    else:
        trigrams[key] = [base_list[i+2]]

def generate_text(length=500, starting_key="Sherlock Holmes"):
    if not trigrams.has_key(starting_key):
        starting_key = "Sherlock Holmes"
        print "That is not a valid key, using 'Sherlock Holmes'"
    output = starting_key.split() #build this up as a word list
    key = starting_key
    for i in range(length):
        output.append(random.sample(trigrams[key],1)[0])
        key = " ".join(output[-2:])
    print textwrap.fill(" ".join(output))

# print trigrams

# for key in trigrams:
#     if len(trigrams[key]) > 10:
#         print key, trigrams[key]

if __name__ == '__main__':
    generate_text()
