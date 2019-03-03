import nltk
from nltk.corpus import wordnet
v = "behaviour"
synsets1=(wordnet.synsets(v))
print(synsets1)

w = "nature"
synsets2=(wordnet.synsets(w))
print(synsets2)

for syn1,syn2 in zip(synsets1,synsets2):
    print(syn1,syn2)
    print(wordnet.wup_similarity(syn1,syn2))
    print()


# syn = synsets[0].name()
#
#
# lemm = synsets[0].lemmas()[0].name()
# print(syn)
# print(lemm)