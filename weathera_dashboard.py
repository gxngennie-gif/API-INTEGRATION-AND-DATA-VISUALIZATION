import requests
import matplotlib.pyplot as plt
from datetime import datetime

latitude=26.6139
longitude=77.2090

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relative_humidity_2m&forecast_days=1"

response=requests.get(url)
data=response.json()
time=data["hourly"]["time"]
tempratures=data["hourly"]["temperature_2m"]
humidity=data["hourly"]["relative_humidity_2m"]

formatted_times=[datetime.strptime(t,"%Y-%m-%dT%H:%M")for t in time]

#temperature graph
plt.figure()
plt.plot(formatted_times,tempratures)
plt.title("hourly temprature-Delhi")
plt.xlabel("time")
plt.ylabel("temprature(°c)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#humidity graph
plt.figure()
plt.plot(formatted_times,humidity)
plt.title("hourly humidity-Delhi")
plt.xlabel("time")
plt.ylabel("humidity(%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
