from bs4 import BeautifulSoup
import requests
import csv

url = "https://notebookspec.com/topchart/notebook.html"
req = requests.get(url)
#print(req)


req.encoding = "utf-8"
soup = BeautifulSoup(req.text, "html.parser")

notebook = soup.find('ul' , class_="top-100-list").find_all('li')



rankls = []
namels = []
pricels = []

for i in notebook:
    rank = i.find('div', class_='num').text.strip()
    name = i.find('div', class_='title').text.strip()
    price = i.find('div', class_='price').text.strip()

    rankls.append(rank)
    namels.append(name)
    pricels.append(price)


#การเก็บข้อมูล
f = open('rank_notebook.csv', 'w', encoding='utf-8', newline="") 

with f:
    writer = csv.writer(f)
    writer.writerow(['อันดับ', 'รายชื่อ', 'ราคาสินค้า'])  # header

    for i in range(len(rankls)):
            writer.writerow([rankls[i], namels[i], pricels[i]])



        