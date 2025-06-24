from bs4 import BeautifulSoup
import requests
import csv #เก็บเป็นfilecsv


url = "https://www.webtoons.com/th/"
req = requests.get(url)
#print(req)


if req.status_code == 200:
    print('successful')
else:
    print('Not successful')

req.encoding = "utf-8"
book = BeautifulSoup(req.text, 'html.parser') #html.parserr
#print(soup.prettify())

books = book.find_all('h2')
#print(courses)

book_list = []
for book in books:
    book_list.append(book.string )
print(book_list)

#csv_column = [['Column Names'],["data or value"]] Course Name
csv_column = [['Books Name'],[book_list]]
f = open('webscripXsoup.csv', 'w', encoding='utf-8', newline="") 
with f:
    writer = csv.writer(f)
    writer.writerow(['Books Name'])  # header

    for name in book_list:
        writer.writerow([name])


