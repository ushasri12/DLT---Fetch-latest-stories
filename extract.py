import requests 
from bs4 import BeautifulSoup

url = "https://time.com/"

with open("times.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

te = soup.find(class_="latest-stories")
se = te.find_all("li")

list1 = []

for i in se:
    d = {}
    he = i.find("h3")
    d["title"] = he.get_text()
    st = i.find("a")
    d["link"] = url + st.get("href")
    list1.append(d)
    
print(list1)