# 단어빈도수를 통한 주요 키워드 그래프화
from matplotlib import pyplot as plt

words = ['2015', '2016', '2017', '2018', '2019']

trump = [1306, 9141, 5238, 3851, 6690]      #1
democrats = [596, 775, 886, 2163, 3533]     #2
sanders = [0, 0, 0, 0, 3569]                #3
harris = [0, 0, 0, 0, 2200]                 #4
republican = [1677, 1427, 1825, 2571, 1286] #5
women = [0, 679, 0, 1153, 1481]             #6
senate = [527, 0, 1531, 1169, 1414]         #7
tax = [864, 0, 3233, 0, 0]                  #8
bill = [584, 0, 1706, 0, 0]                 #9
clinton = [1159, 2021, 0, 0, 0]             #10
obama = [1332, 1455, 588, 0, 1147]          #11 
election = [0, 1439, 584, 1515, 1316]       #12
bush = [879, 0, 0, 0, 0]                    #13  
donald = [0, 974, 0, 0, 0]                  #14
presidentelect = [0, 1237, 0, 0, 0]         #15
biden = [0, 0, 0, 0, 6679]                  #16
warren = [0, 0, 0, 0, 4141]                 #17

plt.xlabel('Year')
plt.ylabel('Number of key words')
plt.title('Identify key words for each year')

plt.plot(words, trump, marker='o')
plt.plot(words, democrats, marker='o')
plt.plot(words, sanders, marker='o')
plt.plot(words, harris, marker='o')
plt.plot(words, republican, marker='o')
plt.plot(words, women, marker='o')
plt.plot(words, senate, marker='o')
plt.plot(words, tax, marker='o')
plt.plot(words, bill, marker='o')
plt.plot(words, clinton, marker='o')
plt.plot(words, biden, color='GreenYellow', marker='o')
plt.plot(words, warren, color='HotPink', marker='o')
plt.plot(words, obama, color='Aqua', marker='o')
plt.plot(words, election, color='Aquamarine', marker='o')
plt.plot(words, bush, color='Black', marker='o')
plt.plot(words, donald, color='Blue', marker='o')
plt.plot(words, presidentelect, color='CadetBlue', marker='o')

plt.legend(['trump','democrats','sanders','harris','republican','women','senate','tax','bill','clinton','biden','warren','obama','election','bush','donald','presidentelect'], loc = 0)
# plt.savefig('C:\\Users\\최정경\\2019python\\wordgraph.png')
plt.show()