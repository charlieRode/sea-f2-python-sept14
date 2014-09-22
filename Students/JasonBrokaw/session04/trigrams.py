import urllib #, string

base_text_file = urllib.urlopen(u"http://codefellows.github.io/sea-c15-python/_downloads/sherlock.txt")

base_text = base_text_file.read()

base_text_file.close()

#Maybe do some cleanup here; need to look more carefully at the file to figure that out

# extra_punctuation = string.punctuation.strip("'-") #Leave some in

# base_text = base_text.strip(extra_punctuation)

base_list = base_text.split()

trigrams = {} #Each key will be a pair of words, and the value will be a set (no repeats) of words that follow that pair

for i in range(len(base_list) - 2):
    key = " ".join(base_list[i:i+2])
    if trigrams.has_key(key):
        trigrams[key].add(base_list[i+2])
    else:
        trigrams[key] = set(base_list[i+2])

# print trigrams

# for key in trigrams:
#     if len(trigrams[key]) > 10:
#         print key, trigrams[key]


