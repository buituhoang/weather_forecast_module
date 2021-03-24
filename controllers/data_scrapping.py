from bs4 import BeautifulSoup
import requests 

class data_scrapping:
    def __init__(self):
        self.data = []

    def get_weather(self):
        file = requests.get('https://weather.com/en-GB/weather/tenday/l/21.00,105.84')
        soup = BeautifulSoup(file.text, 'html.parser')

        list =[]
        content = soup.find_all("div", {"data-testid": "DetailsSummary"})

        for items in content: 
            dict = {} 
            day = items.find_all("span")
            try:
                dict["high_temp"]= int(day[0].text.split('°')[0])
            except:
                dict["high_temp"] = ""
            try:
                dict["low_temp"]= int(day[2].text.split('°')[0])
            except:
                dict["low_temp"] = ""
            try:
                dict["weather"]= day[3].text.split('/')[0].replace('AM ','')
            except:
                dict["weather"] = day[3].text.replace('PM ', '')
            try:
                dict["rain_chance"]= int(day[4].text.split('%')[0])
            except:
                dict["rain_chance"] = ""
            try:
                dict["wind_speed"]= round(int(day[5].text.split(' ')[1])*1.609344,1)
            except:
                dict["wind_speed"]= ""
            list.append(dict) 
        self.data = list
        
