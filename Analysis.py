# 전처리 + 단어 빈도 출력 + WordCloud 생성
import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
import re
import stop_word

# 전처리 기능 함수
def OptimizeText(readData):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》—“”_]', '', readData)
    shortword = re.compile(r'\W*\b\w{1,2}\b')
    text = shortword.sub('', text)
    return text

# 크롤링 한 기사 파일 열고 문자열 변수에 담기
f = open('C:\\Users\\최정경\\2019python\\nyt\\2015all.csv', 'r', encoding='utf-8')
lines = f.readline()
string = ""
while(lines):
    string += lines
    lines = f.readline()   
f.close()
# 불용어 제거 적용 및 전처리화 과정
newstopwords = stop_word.stopwords
tokenizer = RegexpTokenizer('[\w]+')
words = string.lower()
words = OptimizeText(words)
tokens = tokenizer.tokenize(words)
# 전처리 된 텍스트 토큰화
stopped_tokens = [i for i in list((tokens)) if not i in newstopwords]
stopped_tokens2 =[i for i in stopped_tokens if len(i)>1]
# 각 단어 등장 빈도수 출력
print(pd.Series(stopped_tokens2).value_counts().head(60))

# ----------------------------------------------------------------

# 단어 구름 생성
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt

font_path = 'C:/Windows/Fonts/HMKMMAG.TTF'
wordcloud = WordCloud(
   font_path = font_path,
   width = 800,
   height = 800,
   background_color = 'white'
)
count = Counter(stopped_tokens2)
wordcloud = wordcloud.generate_from_frequencies(count)

def __array__(self):
   """Convert to numpy array.
   Returns
   ------
   image : no-array size (width, height,3)
      Word cloud image as numpy matrix.
   """
   return self.to_array()
   
def to_array(self):
   """Convert to numpy array.
   Returns
   ------
   image : no-array size (width, height, 3)
      Word cloud image as numpy matrix.
   """
   return np.array(self.to_image())
array = wordcloud.to_array()

fig = plt.figure(figsize = (10,10))
plt.imshow(array, interpolation="bilinear")
plt.show()
fig.savefig('C:\\Users\\최정경\\2019python\\nyt\\2015wordcloud.png')