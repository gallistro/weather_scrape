import requests
from bs4 import BeautifulSoup
import time
import os

while True:
    os.system('clear')
    r = requests.get("https://www.wunderground.com/weather/us/nj/moorestown-township/KNJMOORE24")
    soup = BeautifulSoup(r.content, "html.parser")

    temp_span = soup.find_all('span', class_="wu-value wu-value-to")
    temp = temp_span[6].contents[0]

    condition_div = soup.find('div', class_="condition-icon")
    condition_p = condition_div.find('p')
    condition = condition_p.contents[0]

    os.system("cowsay" + " " + temp + "f " + condition)
    #print(temp + "F " + condition)
    time.sleep(300)
