import nltk
#nltk.download('wordnet')
from nltk.tokenize import sent_tokenize,word_tokenize
sentence= ("coffe is a better therapy")
word_tok=word_tokenize(sentence)
print(word_tok)
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

p_stemmer = PorterStemmer()
l_stemmer= LancasterStemmer()
s_stemmer = SnowballStemmer("english")
lemmatize= WordNetLemmatizer()
list=['maximum','presumably','multiply','provision','Owed','ear','saying','crying','string','meant','cement','was','study','went']
# for value in list:
#     #print(p_stemmer.stem(value))
#     #print(s_stemmer.stem(value))
#     #print(l_stemmer.stem(value))
#     print(lemmatize.lemmatize(value))
#
#
#
#     print("\n\n")

print(lemmatize.lemmatize("went",pos='v'))
