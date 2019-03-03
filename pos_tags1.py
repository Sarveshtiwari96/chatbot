import nltk
#nltk.download('averaged_perceptron_tagger')
#nltk.download('tagsets')
import nltk.tokenize
from nltk.tokenize import  sent_tokenize,word_tokenize
sentence= ("dddcbwjk hwdneueh ncechonwui huiqhcwci")
word_tok=word_tokenize(sentence)
print(word_tok)
#for sent in sent_tok:
print(nltk.pos_tag(word_tok))
nltk.help.upenn_tagset('NN')

