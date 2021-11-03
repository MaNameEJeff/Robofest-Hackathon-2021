import requests
import json

url = "https://robofest-2021-iot-default-rtdb.firebaseio.com/.json"

querystring = {"auth":"wqBgEeljshmju5p0lgkoIjK0ju3OL9tE6rKensDh"}

response = requests.request("GET", url, params=querystring)

json_data = json.loads(response.text)

print("Air Quality" + " -> " + str(json_data["Device 1"]["Air Quality"]))
print("Humidity" + " -> " + str(json_data["Device 2"]["Humidity"]) + " %")
print("Temperature" + " -> " + str(json_data["Device 3"]["Temperature"]) + " °C")