from bs4 import BeautifulSoup 
import requests

html_text=requests.get('https://www.scrapethissite.com/pages/forms/').text
soup=BeautifulSoup(html_text,'lxml')
table_data=soup.find_all('table',class_='table')
print(table_data)
