from bs4 import BeautifulSoup
import requests

# url = 'C:/Users/Admin/EXAM/PARSER/Parser/index.html'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# label = soup.find('label').text
# print(label)

with open("C:/Users/Admin/EXAM/PARSER/Parser/index.html") as fp:
    soup = BeautifulSoup(fp)

soup = BeautifulSoup("<body>h2</body>")