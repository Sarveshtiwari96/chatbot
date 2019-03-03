import nltk
#nltk.download("punkt") //for downloading punk it package
import nltk.tokenize
from nltk.tokenize import sent_tokenize,word_tokenize
sentence = input("Enter: ")
sent_tok=(sent_tokenize(sentence))
for sent in sent_tok:
    print("sentence:{}", word_tokenize(sent))
    print(sent.split())

