import requests 
from bs4 import BeautifulSoup

url = "https://www.timeanddate.com/worldclock/fullscreen.html?n=246"

r = requests.get(url).text

soup = BeautifulSoup(r, 'html.parser')

ir_date = soup.find('div' , id='i_date')
ir_clock = soup.find('div' , id = 'i_time')
i = 0
print (ir_date.text)

while i<=1:
	i = i+1
	print (ir_clock.text)

