import requests
import json
print ("fuck yes")


# Get the response from the API endpoint.
response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=10d630426bead83db6df7d582a4c2e73")
data = response.json()
new_data = json.loads(data)
print (response.content)


str(new_data["description"])