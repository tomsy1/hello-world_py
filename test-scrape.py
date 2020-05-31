import requests
from bs4 import BeautifulSoup
import datetime

page = requests.get("https://www.bbc.co.uk/weather/2135171")
soup = BeautifulSoup(page.content, 'html.parser')
weather_desc_today = soup.find(class_="wr-day__weather-type-description").get_text()
weather_location = soup.find('h1').find(text=True)


def hours():
    if 'Sunny' in weather_desc_today:
        return("Sunny")
    else:
        if 'cloudy' in weather_desc_today:
            return ("Cloudy")
        else:
            if 'rain' in weather_desc_today:
                return ("Rainy")
weather_today = hours()
fname = input ("What is your first name? ")
lname = input ("What is your surname? ")
fname_length = len(fname)
lname_length = len(lname)
name_char = (fname_length * lname_length)
now = datetime.datetime.now()

print ("Hello " + fname + " " + lname + "! How are you doing on this " + weather_today.lower() + " " + str(now.strftime("%A")) + " in " + weather_location +"?")
print ("Did you know your first name starts with the letter " + fname[0] + " and there are " + str(fname_length) + " characters!")
print ("The number of characters " + str(name_char))

