# 뉴욕타임즈 OPEN API를 통한 기사 추출 및 파일에 내용 저장
import requests
from bs4 import BeautifulSoup
import pprint as pp
import json
import time
import csv

# &fq={filter} , filter = 'news_desk:("Politics")' or 'news_desk:("Economy")'---> session : politics, economy
# api이용해서 긁어온 url csv파일에 저장 
web_urls = []
api_key = ''
for i in range(90, 100):
   url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={query}&begin_date={begin}&end_date={end}&page={page}&api-key={yourkey}'.format(query = 'Politics', begin = 20150101, end = 20151231, page = i, yourkey = api_key)
    
   resp = requests.get(url)
   resp.json()
   resp_dic = json.loads(resp.text)
   resp_dic['response']['docs']
   len(resp_dic['response']['docs'])
   web_urls += [ x['web_url'] for x in resp_dic['response']['docs'] ]
       
print(len(web_urls))    
print(web_urls)

# 기사 내용 파일에 저장
f_output = open("C:\\Users\\최정경\\2019python\\nyt\\2015all.csv",'w', newline='',encoding = "utf-8")
csv_writer = csv.writer(f_output)
csv_writer.writerow(['헤드라인', '본문'])
p_list = []
for url in web_urls:
   resp = requests.get(url)
   soup = BeautifulSoup(resp.text,'html.parser')
   body = soup.select('div.css-53u6y8')
   leng = len(body)
   con = ""
   for i in range(0, leng):
      p = body[i]
      pind = p.find_all('p')
      for j in pind:
         t = j.get_text()
         con += t
   csv_writer.writerow(["제목", con])
f_output.close()
