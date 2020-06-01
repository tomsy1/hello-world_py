import requests
from bs4 import BeautifulSoup
import datetime

story_live = True

where_are_you = input("Where are you today? ").upper()
locations = {
"COULSDON":2652249,
"LONDON":2643743,
"MUNICH":2867714,
"MOSCOW":524901,
}
location_id = locations.get(where_are_you,"nah")

while location_id == ("nah"):
    try_again = input("The destination " + where_are_you.capitalize() + " has not been recognised would you like to try again? ")
    if try_again == ("y"):
        where_are_you = input("Where are you today? ").upper()
    else:
        break
    location_id = locations.get(where_are_you, "nah")


if location_id == "nah":
    story_live = False
else:
    page = requests.get("https://www.bbc.co.uk/weather/" + str(location_id))
    soup = BeautifulSoup(page.content, 'html.parser')
    weather_desc_today = soup.find(class_="wr-day__weather-type-description").get_text()
    weather_location = soup.find('h1').find(text=True)
    now = datetime.datetime.now()

def hours():
    if 'Sunny' in weather_desc_today:
        return("Sunny")
    else:
        if 'cloudy' in weather_desc_today:
            return ("Cloudy")
        else:
            if 'rain' in weather_desc_today:
                return ("Rainy")
def time_period():
    if now.hour > 00 and now.hour < 12:
        return ("Morning")
    else:
        if now.hour >= 12 and now.hour < 18:
            return("Afternoon")
        else:
            if now.hour >= 18 and now.hour < 22:
                return("Evening")
            else:
                if now.hour == 22 and now.hour <=00:
                    return("Night")
#where_are_you = input("Where are you today? ")
#print(locations[where_are_you])
#location_id = locations[where_are_you]
#print(location_id)



def story():
    fname = input("What is your first name? ")
    lname = input("What is your surname? ")
    weather_today = hours()
    fname_length = len(fname)
    lname_length = len(lname)
    name_char = (fname_length * lname_length)
    print ("Hello " + fname + " " + lname + "! How are you doing on this " + weather_today.lower() + " " + str(now.strftime("%A")) + " " + str(time_period().lower()) +" in " + weather_location +"?")
    print ("Did you know your first name starts with the letter " + fname[0] + " and there are " + str(fname_length) + " characters!")
    print ("The number of characters " + str(name_char))


if story_live:
    story()
else:
    print ("The story is not yet live")