import re
import requests
from bs4 import BeautifulSoup
import time
a=120
f = open("result.txt","a")
while a<130:
	a+=1
	url="http://dm.sakinorva.net/view?id="+str(a)
	page=requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	div=soup.find_all("div", {"class": "thread_box"})[0]
	name = div.p.text
	attr1=div.find_all('div')[1].get("style").split(";")[2].split(")")[-2]
	attr2=(div.find_all('div')[2].get("style").split(";")[2].split(")")[-2])
	attr3=(div.find_all('div')[3].get("style").split(";")[2].split(")")[-2])
	attr4=(div.find_all('div')[4].get("style").split(";")[2].split(")")[-2])
	f.write(name)
	f.write(",")
	f.write(attr1)
	f.write(",")
	f.write(attr2)
	f.write(",")
	f.write(attr3)
	f.write(",")
	f.write(attr4)
	
	f.write("\n")
	print(name+"'s profile download complete,5s cooldown")
	time.sleep(5)
f.close()













































	