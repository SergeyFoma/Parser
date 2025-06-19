from bs4 import BeautifulSoup 
import requests
import lxml
from datetime import datetime

now=datetime.now()
print(now.strftime("%d.%m.%Y"))

url = "http://127.0.0.1:8000/answer2/"
response = requests.get(url)
# print(response)
bs=BeautifulSoup(response.text,'lxml')
# print(soup)

temp2=bs.find(class_='result').find('h2')
with open('resultat.txt','a',encoding='UTF-8')as f:
    f.write(f'{temp2.text}\n')

temp3=bs.find(class_='result').find_all('p')
for x in temp3:
    print(x.text)
    with open('resultat.txt','a',encoding='UTF-8')as f:
        f.write(f'{x.text}\n')




# with open('C:/Users/Fomenko.SM/EXAM_PSO3/PARSER/Parser/index.html',encoding='UTF-8') as file:
# 	src=file.read()

# soup=bs(src,'lxml')
# s=soup.find_all('h2')
# for i in s:
#     print(i.text)