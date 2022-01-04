# 토픽모델링(LDA)
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim import corpora,models
import gensim
from nltk.tokenize import RegexpTokenizer
import stop_word
import re

# 전처리 
def OptimizeText(readData):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》—“”_]', '', readData)
    shortword = re.compile(r'\W*\b\w{1,2}\b')
    text = shortword.sub('', text)
    return text

newstopwords = stop_word.stopwords
tokenizer = RegexpTokenizer('[\w]+')

#기사본문 불러오기
f = open('C:\\Users\\최정경\\2019python\\nyt\\All.txt', 'r', encoding='utf-8')
lines = f.readline()
string = ""
while(lines):
    string += lines
    lines = f.readline()   
f.close()
string = string.lower()
string = OptimizeText(string)

doc_set = [string]
texts = []

# LDA
for w in doc_set:
   raw = w
   tokens = tokenizer.tokenize(raw)
   stopped_tokens = [i for i in tokens if not i in newstopwords]
   texts.append(stopped_tokens)
   dictionary = corpora.Dictionary(texts)
   corpus = [dictionary.doc2bow(text) for text in texts]
   ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=5, id2word = dictionary)
   print(ldamodel.print_topics(num_words=7))
   print(ldamodel.get_document_topics(corpus)[0])   
#-----------------------
# import matplotlib.pyplot as plt
# perplexity_values=[]
# for i in range(40,100):
#    ldamodel= gensim.models.ldamodel.LdaModel(corpus,num_topics=i,
#    id2word=dictionary)
#    perplexity_values.append(ldamodel.log_perplexity(corpus))
# x = range(40,100)
# plt.plot(x, perplexity_values)
# plt.xlabel("Number of topics")
# plt.ylabel("Perplexity score")
# plt.show()

   
   